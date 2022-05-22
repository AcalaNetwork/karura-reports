from substrateinterface import SubstrateInterface
# substrate.rpc_request("system_properties", []).get('result')

from datetime import datetime
import pandas as pd
import numpy as np
from datetime import date
import json

def unique(list1):
    x = np.array(list1)
    print(np.unique(x))
        
# Oliver Corbisiero
# https://github.com/polkadot-js/apps/blob/eb19203f0af55090be3023402f47db8773252cb7/packages/apps-config/src/endpoints/productionRelayPolkadot.ts#L30-L294
# https://github.com/polkadot-js/apps/blob/eb19203f0af55090be3023402f47db8773252cb7/packages/apps-config/src/endpoints/productionRelayKusama.ts#L31-L400

kusama ={
    'Bifrost': 'wss://bifrost-rpc.liebi.com/ws',
    'Aleph Zero': 'wss://ws.azero.dev',
    'Altair': 'wss://fullnode.altair.centrifuge.io',
    'Basilisk': 'wss://rpc-01.basilisk.hydradx.io',
    'BitcountryPioneer': 'wss://pioneer-1-rpc.bit.country',
    'Automata': 'wss://api.ata.network',
    # 'Centrifuge Standalone [Archived]': 'wss://fullnode.centrifuge.io',
    'Calamari': 'wss://ws.calamari.systems/',
    'ChainX': 'wss://mainnet.chainx.org/ws',
    'Crab': 'wss://crab-parachain-rpc.darwinia.network/',
    # 'Competitors Club': 'wss://node0.competitors.club/wss',
    'Creditcoin': 'wss://mainnet.creditcoin.network',
    # 'Crown Sterling': 'wss://blockchain.crownsterling.io',
    # 'Crust Network': 'wss://rpc.crust.network',
    # 'Darwinia': 'wss://rpc.darwinia.network',
    'Darwinia Crab': 'wss://crab-rpc.darwinia.network',
    # 'Dock': 'wss://mainnet-node.dock.io',
    'Encointer': 'wss://kusama.api.encointer.org',
    # 'Edgeware': 'wss://mainnet.edgewa.re',
    'Efinity': 'wss://rpc.efinity.io',
    # 'Equilibrium': 'wss://node.equilibrium.io',
    'Genshiro': 'wss://node.genshiro.io',
    'Heiko': 'wss://parallel-heiko.api.onfinality.io/public-ws',
    # 'Hanonycash': 'wss://rpc.hanonycash.com',
    # 'HydraDX': 'wss://rpc-01.snakenet.hydradx.io',
    'Integritee': 'wss://kusama.api.integritee.network',
    'Khala': 'wss://khala-api.phala.network/ws',
    'Kico': 'wss://rpc.kico.dico.io',
    'Kpron': 'wss://kusama-kpron-rpc.apron.network/',
    'Karura': 'wss://karura.polkawallet.io',
    'Khala': 'wss://khala-api.phala.network/ws',
    'Kintsugi': 'wss://api-kusama.interlay.io/parachain',
    'Kusama': 'wss://kusama.api.onfinality.io/public-ws',
    # 'Kulupu': 'wss://rpc.kulupu.corepaper.org/ws',
    # 'Kusari': 'wss://ws.kusari.network',
    'Litmus': 'wss://rpc.litmus-parachain.litentry.io',
    'LoomNetwork': 'wss://kusama.dappchains.com',
    'Mangata': 'wss://v4-prod-collator-01.mangatafinance.cloud',
    'Mars': 'wss://wss.mars.aresprotocol.io',
    # 'MathChain': 'wss://mathchain-asia.maiziqianbao.net/ws',
    'MiniX': 'wss://minichain-mainnet.coming.chat/ws',
    'Moonriver': 'wss://wss.api.moonriver.moonbeam.network',
    'Neatcoin': 'wss://rpc.neatcoin.org/ws',
    # 'NFTMart': 'wss://mainnet.nftmart.io/rpc/ws',
    'Nodle': 'wss://main3.nodleprotocol.io',
    'Heiko': 'wss://heiko-rpc.parallel.fi',
    # 'Plasm': 'wss://rpc.plasmnet.io/',
    # 'Polkadex': 'wss://mainnet.polkadex.trade',
    # 'Polymesh Mainnet': 'wss://mainnet-rpc.polymesh.network',
    'Picasso': 'wss://picasso-rpc.composable.finance',
    'Pichiu': 'wss://kusama.kylin-node.co.uk',
    'Polkasmith': 'wss://wss-polkasmith.polkafoundry.com',
    'Quartz': 'wss://quartz.unique.network',
    # 'RioChain': 'wss://node.v1.riochain.io',
    'Robonomics': 'wss://kusama.rpc.robonomics.network/',
    'Shadow': 'wss://rpc-shadow.crust.network/',
    'Sakura': 'wss://api-sakura.clover.finance',
    'Sora_ksm': 'wss://ws.parachain-collator-1.c1.sora2.soramitsu.co.jp',
    'Subgame': 'wss://gamma.subgame.org/',
    'Subsocial': 'wss://para.subsocial.network',
    'SherpaX': 'wss://mainnet.sherpax.io',
    'Shiden': 'wss://shiden.api.onfinality.io/public-ws',
    'Statemine': 'wss://statemine-rpc.polkadot.io',
    'Stafi': 'wss://mainnet-rpc.stafi.io',
    # 'SORA': 'wss://ws.mof.sora.org',
    # 'Spanner': 'wss://wss.spannerprotocol.com',
    # 'SubGame': 'wss://mainnet.subgame.org/',
    # 'Subsocial': 'wss://rpc.subsocial.network',
    # 'Swapdex': 'wss://ws.swapdex.network',
    # 'UniArts': 'wss://mainnet.uniarts.vip:9443',
    'Unorthodox': 'wss://rpc.kusama.standard.tech',
    # 'Westlake': 'wss://westlake.datahighway.com'
    'Zeitgeist': 'wss://rpc-0.zeitgeist.pm'}

polkadot = {'Acala': 'wss://acala-rpc-0.aca-api.network',
            # 'Ares Odyssey': 'wss://wss.odyssey.aresprotocol.io',
            'Astar': 'wss://rpc.astar.network',
            'Bifrost': 'wss://bifrost-rpc.liebi.com/ws',
            'Centrifuge': 'wss://fullnode.parachain.centrifuge.io',
            'Clover': 'wss://rpc-para.clover.finance',
            # 'Coinversation': 'wss://rpc.coinversation.io/',
            'Composable Finance': 'wss://rpc.composable.finance',
            'Crust': 'wss://rpc.crust.network',
            'Darwinia': 'wss://parachain-rpc.darwinia.network',
            'Efinity': 'wss://rpc.efinity.io',
            'Equilibrium': 'wss://node.pol.equilibrium.io/',
            'Geminis': 'wss://rpc.geminis.network',
            'HydraDX': 'wss://rpc-01.hydradx.io',
            'Interlay': 'wss://api.interlay.io/parachain',
            'Kapex': 'wss://k-ui.kapex.network',
            # 'Litentry': 'wss://parachain.litentry.io',
            'Manta': 'wss://kuhlii.manta.systems',
            'Moonbeam': 'wss://wss.api.moonbeam.network',
            'Nodle': 'wss://nodle-parachain.api.onfinality.io/public-ws',
            'Odyssey': 'wss://wss.odyssey.aresprotocol.io',
            # 'OriginTrail Parachain': 'wss://parachain-rpc.origin-trail.network',
            'Parallel': 'wss://parallel.api.onfinality.io/public-ws',
            'Phala': 'wss://api.phala.network/ws',
            'Polkadex': 'wss://polkadex.api.onfinality.io/public-ws',
            # 'SubDAO': 'wss://parachain-rpc.subdao.org',
            # 'SubGame Gamma': 'wss://gamma.subgame.org/',
            'Unique Network': 'wss://ws.unique.network/',
            'Statemint': 'wss://statemint-rpc.polkadot.io',
            'Polkadot': 'wss://rpc.polkadot.io'}

    
wss_map = kusama | polkadot
wss_map_df = pd.DataFrame(list(wss_map.items()),columns = ['Name','url'])

def get_token_issuance(url):
    data = []
    source = "Tokens"
    try:
        substrate = SubstrateInterface(url)
        hash = substrate.get_chain_finalised_head()
        timestamp = substrate.query(module='Timestamp',storage_function='Now',block_hash=hash).value
        block = substrate.get_block_number(hash)
        result = substrate.query_map(module='Tokens',storage_function='TotalIssuance')
        for res in result:
            # print(f"{url} " + json.dumps(res[0].value))
            try:
                token = res[0].value
                amount = res[1].value            
                outi = {"url": url, "Module": source, "Block": block, "Time": timestamp, 'Token': token, 'Amount': amount}
                data.append(outi)
            except Exception as e:
                token = None
        
            return data
    except Exception as e:
        print("No Tokens for " + url)

def get_balances_issuance(url):
    data = []
    source = "Balances"
    try:
        substrate = SubstrateInterface(url)
        hash = substrate.get_chain_finalised_head()
        timestamp = substrate.query(module='Timestamp',storage_function='Now',block_hash=hash).value
        block = substrate.get_block_number(hash)
        token = substrate.properties['tokenSymbol']
        amount = substrate.query(module='Balances',storage_function='TotalIssuance').value
        outi = {"url": url, "Module": source, "Block": block, "Time": timestamp, 'Token': token, 'Amount': amount}
        data.append(outi)
        return data
    except Exception as e:
        print("No Balances for " + url)


# shiden astar moonbeam moonriver
def get_assets_supply(url):
    data = []
    source = "Assets"
    try:
        substrate = SubstrateInterface(url)
        hash = substrate.get_chain_finalised_head()
        timestamp = substrate.query(module='Timestamp',storage_function='Now',block_hash=hash).value
        block = substrate.get_block_number(hash)
        result = substrate.query_map(module='Assets',storage_function='Asset')
        for res in result:
            try:
                token = res[0].value
                amount = res[1].value['supply']          
                outi = {"url": url, "Module": source, "Block": block, "Time": timestamp, 'Token': token, 'Amount': amount}
                data.append(outi)
            except Exception as e:
                token = None
        return data
    except Exception as e:
        print("No Assets for " + url)
    
def get_homa_stakingLedger(url):
    data = []
    source = "Assets"
    try:
        # url = 'wss://karura.polkawallet.io'
        substrate = SubstrateInterface(url)
        hash = substrate.get_chain_finalised_head()
        timestamp = substrate.query(module='Timestamp',storage_function='Now',block_hash=hash).value
        block = substrate.get_block_number(hash)
        result = substrate.query_map(module='Homa',storage_function='StakingLedgers')
        if url == wss_map['Karura']:
            token = 'KSM (on Homa)'
        elif url == wss_map['Acala']:
            token = 'DOT (on Homa)'
        else:
            token = None
        amount = 0
        for res in result:
            amount += res[1].value['bonded']          
        
        if token != None:
            outi = {"url": url, "Module": source, "Block": block, "Time": timestamp, 'Token': token, 'Amount': amount}
            data.append(outi)
            return data
    except Exception as e:
        print("No Assets for " + url)


today = date.today().strftime("%Y%m%d")
fname = f"~/R_HOME/karura_dashboard/tokens_{today}.csv"

mode = "w"
header = True
for key in wss_map:
    url = wss_map[key]
    # url = 'wss://statemine-rpc.polkadot.io'
    out1 = get_token_issuance(url)
    if out1 != None and out1 != []:
        out = pd.DataFrame(out1).merge(wss_map_df, on='url')
        out['Time'] = pd.to_datetime(out['Time'],unit='ms').dt.date
        out.to_csv(fname, mode = mode, index = False, header = header)
        mode = "a"
        header = False
        del out, out1
    out2 = get_balances_issuance(url)
    if out2 != None and out2 != []:
        out = pd.DataFrame(out2).merge(wss_map_df, on='url')
        out['Time'] = pd.to_datetime(out['Time'],unit='ms').dt.date
        out.to_csv(fname, mode = mode, index = False, header = header)
        mode = "a"
        header = False
        del out, out2
    out3 = get_assets_supply(url)
    if out3 != None and out3 != []:
        out = pd.DataFrame(out3).merge(wss_map_df, on='url')
        out['Time'] = pd.to_datetime(out['Time'],unit='ms').dt.date
        out.to_csv(fname, mode = mode, index = False, header = header)
        mode = "a"
        header = False
        del out, out3
    if url == wss_map['Karura'] or  url == wss_map['Acala']:
        out4 = get_homa_stakingLedger(url)
        out = pd.DataFrame(out4).merge(wss_map_df, on='url')
        out['Time'] = pd.to_datetime(out['Time'],unit='ms').dt.date
        out.to_csv(fname, mode = mode, index = False, header = header)
        mode = "a"
        header = False
        del out, out4
        



