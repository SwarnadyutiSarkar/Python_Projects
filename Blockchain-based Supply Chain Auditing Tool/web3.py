from web3 import Web3
import json

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('https://your-infura-or-node-url'))

# Load your contract ABI and address
with open('SupplyChainAuditABI.json') as f:
    abi = json.load(f)

contract_address = '0xYourContractAddress'
supply_chain_contract = w3.eth.contract(address=contract_address, abi=abi)

# Function to create an item
def create_item(name, status, location, private_key, account):
    tx = supply_chain_contract.functions.createItem(name, status, location).buildTransaction({
        'from': account,
        'nonce': w3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Function to update an item
def update_item(item_id, status, location, private_key, account):
    tx = supply_chain_contract.functions.updateItem(item_id, status, location).buildTransaction({
        'from': account,
        'nonce': w3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Function to get item details
def get_item(item_id):
    return supply_chain_contract.functions.getItem(item_id).call()

# Example usage
if __name__ == "__main__":
    account = '0xYourAccountAddress'
    private_key = '0xYourPrivateKey'

    # Create an item
    create_tx_hash = create_item("Product A", "Manufactured", "Factory A", private_key, account)
    print(f"Item created: {create_tx_hash.hex()}")

    # Update the item
    update_tx_hash = update_item(1, "In Transit", "Warehouse B", private_key, account)
    print(f"Item updated: {update_tx_hash.hex()}")

    # Get item details
    item_details = get_item(1)
    print(f"Item details: Name: {item_details[0]}, Status: {item_details[1]}, Owner: {item_details[2]}, Timestamp: {item_details[3]}, Location: {item_details[4]}")
