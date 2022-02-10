qry <- Query$new()
qry$query('dexActions', '{
    query {
      dexActions(filter: {timestamp: {greaterThanOrEqualTo: "' %+% mindate %+% '"}}
            			first: 100
      						offset: ' %+% offset %+% ') {
        nodes {
          timestamp
          id
          nodeId
          accountId
          type
          token0Id
          token1Id
          token0Amount
          token1Amount
          volumeUSD
          extrinsicId
          data
        }
      }
    }
  }')
result <- cli$exec(qry$queries$dexActions) %>%
  fromJSON(flatten=TRUE)
res <- as.data.table(result$data$query$dexActions$nodes)
