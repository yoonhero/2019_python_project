from web3 import Web3
infura_url = "https://mainnet.infura.io/v3/953247d0c42b419aa3416810d625cc8c"
web = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())