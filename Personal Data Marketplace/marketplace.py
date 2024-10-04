from web3 import Web3
import json

# Connect to local Ethereum blockchain
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))  # Ganache default address

# Ensure connection
if not w3.isConnected():
    print("Failed to connect to the blockchain")
    exit()

# Set up the contract
with open('PersonalDataMarketplace.json') as f:
    contract_json = json.load(f)  # Load the contract ABI
    contract_abi = contract_json['abi']
    contract_address = 'YOUR_CONTRACT_ADDRESS'  # Replace with your deployed contract address

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Listing data
def list_data(title, description, price, account):
    tx_hash = contract.functions.listData(title, description, price).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Data listed successfully")

# Buying data
def buy_data(listing_id, price, account):
    tx_hash = contract.functions.buyData(listing_id).transact({
        'from': account,
        'value': w3.toWei(price, 'ether')  # Assuming price is in Ether
    })
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Data purchased successfully")

# Example usage
if __name__ == '__main__':
    # Replace with your Ganache account addresses
    account1 = 'YOUR_ACCOUNT_1_ADDRESS'
    account2 = 'YOUR_ACCOUNT_2_ADDRESS'

    # List some data
    list_data("Personal Data", "Description of personal data", w3.toWei(0.1, 'ether'), account1)

    # Buy the data (listing ID is 1 in this example)
    buy_data(1, 0.1, account2)
