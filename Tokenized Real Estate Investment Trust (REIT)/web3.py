from web3 import Web3
import json

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('https://your-infura-or-node-url'))

# Load your contract ABI and address
with open('TokenizedREITABI.json') as f:
    abi = json.load(f)

contract_address = '0xYourContractAddress'
reit_contract = w3.eth.contract(address=contract_address, abi=abi)

# Function to add a property
def add_property(name, value, shares, private_key, account):
    tx = reit_contract.functions.addProperty(name, value, shares).buildTransaction({
        'from': account,
        'nonce': w3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Function to invest in a property
def invest_in_property(property_id, shares, private_key, account):
    tx = reit_contract.functions.investInProperty(property_id, shares).buildTransaction({
        'from': account,
        'nonce': w3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Function to pay dividends
def pay_dividends(property_id, amount, private_key, account):
    tx = reit_contract.functions.payDividends(property_id, amount).buildTransaction({
        'from': account,
        'value': w3.toWei(amount, 'ether'),
        'nonce': w3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Example usage
if __name__ == "__main__":
    account = '0xYourAccountAddress'
    private_key = '0xYourPrivateKey'

    # Add a property
    add_tx_hash = add_property("Luxury Apartment", 100 ether, 1000, private_key, account)
    print(f"Property added: {add_tx_hash.hex()}")

    # Invest in a property
    invest_tx_hash = invest_in_property(0, 100, private_key, account)
    print(f"Investment made: {invest_tx_hash.hex()}")

    # Pay dividends
    dividend_tx_hash = pay_dividends(0, 10 ether, private_key, account)
    print(f"Dividends paid: {dividend_tx_hash.hex()}")
