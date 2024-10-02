from web3 import Web3

# Connect to Ethereum node (e.g., Infura)
infura_url = 'YOUR_INFURA_URL'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected
if not web3.isConnected():
    print("Failed to connect to Ethereum network!")
    exit()

# Your smart contract address and ABI
contract_address = 'YOUR_CONTRACT_ADDRESS'
contract_abi = [
    # Insert the ABI of your contract here
]

# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Replace with your wallet address and private key
my_address = 'YOUR_WALLET_ADDRESS'
private_key = 'YOUR_PRIVATE_KEY'

# Register an IP asset
def register_asset(name, description):
    nonce = web3.eth.getTransactionCount(my_address)
    txn = contract.functions.registerAsset(name, description).buildTransaction({
        'chainId': 3,  # Ropsten network
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
    })
    
    signed_txn = web3.eth.account.signTransaction(txn, private_key=private_key)
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f'Transaction sent: {web3.toHex(txn_hash)}')

# Verify ownership of an IP asset
def verify_ownership(name):
    owner = contract.functions.verifyOwnership(name).call()
    print(f'The owner of "{name}" is: {owner}')

# Example usage
register_asset("My Unique Invention", "A detailed description of my invention.")
verify_ownership("My Unique Invention")
