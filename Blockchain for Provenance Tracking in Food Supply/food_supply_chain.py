from web3 import Web3
import json

# Connect to local Ethereum blockchain
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))  # Ganache default address

# Ensure connection
if not w3.isConnected():
    print("Failed to connect to the blockchain")
    exit()

# Set up the contract
with open('FoodSupplyChain.json') as f:
    contract_json = json.load(f)  # Load the contract ABI
    contract_abi = contract_json['abi']
    contract_address = 'YOUR_CONTRACT_ADDRESS'  # Replace with your deployed contract address

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Create a food item
def create_food_item(name, origin, account):
    tx_hash = contract.functions.createFoodItem(name, origin).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Food item '{name}' created successfully")

# Update the location of a food item
def update_food_location(item_id, new_location, account):
    tx_hash = contract.functions.updateLocation(item_id, new_location).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Food item ID {item_id} location updated to '{new_location}'")

# Get details of a food item
def get_food_item(item_id):
    item = contract.functions.getFoodItem(item_id).call()
    print(f"Food Item ID: {item_id}")
    print(f"Name: {item[0]}, Origin: {item[1]}, Current Location: {item[2]}, Owner: {item[3]}")
    print(f"History: {item[4]}")

# Example usage
if __name__ == '__main__':
    # Replace with your Ganache account addresses
    account1 = 'YOUR_ACCOUNT_1_ADDRESS'
    account2 = 'YOUR_ACCOUNT_2_ADDRESS'

    # Create a food item
    create_food_item("Tomato", "Farm A", account1)

    # Update the food item's location
    update_food_location(1, "Warehouse 1", account1)

    # Get details of the food item
    get_food_item(1)
