from web3 import Web3
import time

provider_url = "" 
web3 = Web3(Web3.HTTPProvider(provider_url))

contract_address = "CONTRACT_ADDRESS"
contract_abi = []  # import

private_key = ""

contract = web3.eth.contract(address=contract_address, abi=contract_abi)


user_address = "USER_ADDRESS"

current_block_number = web3.eth.blockNumber

randao_value = contract.functions.getRandomNumber().call({'from': user_address})

print(f"Current randao value: {randao_value}")

# Store the randao value in the contract

key = 1
transaction = contract.functions.storeRandomNumber(key).buildTransaction({
    'chainId': web3.eth.chainId,
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'nonce': web3.eth.getTransactionCount(user_address),
})

signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(f"Transaction sent. Tx hash: {web3.toHex(tx_hash)}")

# Wait for the next block
while web3.eth.blockNumber <= current_block_number:
    time.sleep(1)

print("New block mined.")

# Retrieve the updated block hash and timestamp
block_hash_now = contract.functions.blockHashNow().call()
block_timestamp = contract.functions.getBlockHashTimestamp().call()

print(f"New block hash: {block_hash_now}")
print(f"New block timestamp: {block_timestamp}")
