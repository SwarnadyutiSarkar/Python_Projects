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

# Create a project
def create_project(name, goal):
    nonce = web3.eth.getTransactionCount(my_address)
    txn = contract.functions.createProject(name, goal).buildTransaction({
        'chainId': 3,  # Ropsten network
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
    })
    
    signed_txn = web3.eth.account.signTransaction(txn, private_key=private_key)
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f'Transaction sent: {web3.toHex(txn_hash)}')

# Fund a project
def fund_project(project_id, amount):
    nonce = web3.eth.getTransactionCount(my_address)
    txn = contract.functions.fundProject(project_id).buildTransaction({
        'chainId': 3,
        'value': web3.toWei(amount, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
    })
    
    signed_txn = web3.eth.account.signTransaction(txn, private_key=private_key)
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f'Transaction sent: {web3.toHex(txn_hash)}')

# Example usage
create_project("My First Project", web3.toWei(1, 'ether'))
fund_project(1, 0.1)
