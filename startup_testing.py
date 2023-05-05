from web3 import Web3, HTTPProvider
from config import MY_API_TOKEN
connection = Web3(HTTPProvider(f'https://mainnet.infura.io/v3/{MY_API_TOKEN}'))
print ("Latest Ethereum block number", connection.eth.get_block_number())