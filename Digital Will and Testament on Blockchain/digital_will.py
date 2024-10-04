from web3 import Web3
import json

# Connect to local Ethereum blockchain
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))  # Ganache default address

# Ensure connection
if not w3.isConnected():
    print("Failed to connect to the blockchain")
    exit()

# Set up the contract
with open('DigitalWill.json') as f:
    contract_json = json.load(f)  # Load the contract ABI
    contract_abi = contract_json['abi']
    contract_address = 'YOUR_CONTRACT_ADDRESS'  # Replace with your deployed contract address

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Create a digital will
def create_will(content, account):
    tx_hash = contract.functions.createWill(content).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Digital will created successfully")

# Update a digital will
def update_will(will_id, new_content, account):
    tx_hash = contract.functions.updateWill(will_id, new_content).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Digital will updated successfully")

# Revoke a digital will
def revoke_will(will_id, account):
    tx_hash = contract.functions.revokeWill(will_id).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Digital will revoked successfully")

# Get details of a digital will
def get_will(will_id):
    owner, content, is_active = contract.functions.getWill(will_id).call()
    print(f"Will ID: {will_id}")
    print(f"Owner: {owner}, Content: {content}, Active: {is_active}")

# Example usage
if __name__ == '__main__':
    # Replace with your Ganache account addresses
    account1 = 'YOUR_ACCOUNT_1_ADDRESS'
    account2 = 'YOUR_ACCOUNT_2_ADDRESS'

    # Create a digital will
    create_will("This is my last will and testament.", account1)

    # Update the digital will
    update_will(1, "Updated: This is my last will and testament.", account1)

    # Get details of the digital will
    get_will(1)

    # Revoke the digital will
    revoke_will(1, account1)
