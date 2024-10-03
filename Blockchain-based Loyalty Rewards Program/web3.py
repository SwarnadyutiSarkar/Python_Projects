from web3 import Web3
import json

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('https://your-infura-or-node-url'))

# Load your contract ABI and address
with open('LoyaltyRewardsABI.json') as f:
    abi = json.load(f)

contract_address = '0xYourContractAddress'
loyalty_contract = w3.eth.contract(address=contract_address, abi=abi)

# Function to register a user
def register_user(private_key, account):
    tx = loyalty_contract.functions.registerUser().buildTransaction({
        'from': account,
        'nonce': w3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Function to award points
def award_points(user, amount, private_key, account):
    tx = loyalty_contract.functions.awardPoints(user, amount).buildTransaction({
        'from': account,
        'nonce': w3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Function to redeem points
def redeem_points(amount, private_key, account):
    tx = loyalty_contract.functions.redeemPoints(amount).buildTransaction({
        'from': account,
        'nonce': w3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Function to check points
def get_points(account):
    return loyalty_contract.functions.getPoints().call({'from': account})

# Example usage
if __name__ == "__main__":
    account = '0xYourAccountAddress'
    private_key = '0xYourPrivateKey'

    # Register user
    reg_tx_hash = register_user(private_key, account)
    print(f"User registered: {reg_tx_hash.hex()}")

    # Award points
    award_tx_hash = award_points(account, 100, private_key, account)
    print(f"Points awarded: {award_tx_hash.hex()}")

    # Check points
    points = get_points(account)
    print(f"User points: {points}")

    # Redeem points
    redeem_tx_hash = redeem_points(50, private_key, account)
    print(f"Points redeemed: {redeem_tx_hash.hex()}")

    # Check points again
    points = get_points(account)
    print(f"User points after redemption: {points}")
