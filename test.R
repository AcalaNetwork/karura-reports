library(ghql)
getSwaps <- function(endpoint, window) {
  # endpoint <- acala_endpoint; window <- 10
  
  # make a client
  cli <- GraphqlClient$new(url = endpoint)
  mindate <- today(tzone = 'UTC') - window
  
  cursor <- ''
  resList <- list()
  for (i in 1:1000) {
    if (cursor == '') {
      cursorStr <- 'first:100'
    } else {
      cursorStr <- 'first:100 after:"' %+% cursor %+% '"'
    }
    qry <- Query$new()
    qry$query('dexActions', '
    {
      query {
        dexActions (filter: {timestamp: {greaterThanOrEqualTo: "' %+% mindate %+% '"}, type: {equalTo: "swap"}} ' %+% cursorStr %+% ') {
          totalCount
          edges {
            node { timestamp id accountId token0Id token1Id volumeUSD token0Amount token1Amount token0Price token1Price data
            }
            cursor
          }
          pageInfo {
            endCursor
            hasNextPage
          }
        }
      }
    }')
    result <- cli$exec(qry$queries$dexActions)  %>%
      fromJSON(flatten=TRUE)
    cursor <- result$data$query$dexActions$pageInfo$endCursor
    res <- as.data.table(result$data$query$dexActions$edges)
    res[, cursor := NULL]
    
    print(i %+% " " %+% nrow(res))
    resList[[i]] <- res
    if (result$data$query$dexActions$pageInfo$hasNextPage == FALSE) break
  }
  res <- rbindlist(resList)
  setnames(res, old = names(res), new = gsub("node.", "", names(res)))
  
  if (substr(max(res$timestamp), 12, 13) < 23) {
    maxdate <- as.Date(max(res$timestamp))-1
  } else {
    maxdate <- as.Date(max(res$timestamp))
  }
  
  res <- res[timestamp <= maxdate]
  res[, date := as.Date(timestamp)]
  setorder(res, timestamp)
  
  # Replace foreign assets
  res[token0Id == 'fa://0', token0Id := 'RMRK']
  res[token1Id == 'fa://0', token1Id := 'RMRK']
  
  res[token0Id == 'lc://13', token0Id := 'LCDOT']
  res[token1Id == 'lc://13', token1Id := 'LCDOT']
  
  
  if (min(res$pathLength) == 2) res[, pathLength := pathLength - 1]
  # res[, fee := .003 * volumeUSDFloat]
  # res[, feeAdj := .003 * pathLength * volumeUSDFloat]
  
  # Normalize pairs
  res[, pair := paste0(token0Id %+% ":" %+% token1Id)]
  res[token1Id < token0Id, pair := paste0(token1Id %+% ":" %+% token0Id)]
  res[, exclude := token0Id == token1Id]
  res  
  
}



swaps2 <- getSwapsByDay(endpoint="https://api.subquery.network/sq/rogerjbos/karura-swap-data", window)
head(swaps2)
swaps2[volumeUSD < 0]

swaps <- getSwaps(endpoint="https://api.subquery.network/sq/rogerjbos/karura-swap-data", window)
head(swaps)
swaps[volumeUSD < 0]

swaps4 <- getSwaps(endpoint="https://api.subquery.network/sq/rogerjbos/karura-swap-day-data__cm9nZ", window)
head(swaps4)
swaps4[volumeUSD < 0]

swaps5 <- getSwaps(endpoint="https://api.subquery.network/sq/rogerjbos/karura-test", window)
head(swaps5)
swaps5[volumeUSD < 0]





karura_official_endpoint <- "https://api.subquery.network/sq/AcalaNetwork/karura"
swaps3 <- getSwaps(endpoint = karura_official_endpoint, window)
head(swaps3)
swaps3[volumeUSD < 0]

