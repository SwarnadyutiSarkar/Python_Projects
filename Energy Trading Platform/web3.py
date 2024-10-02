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

# Register energy
def register_energy(energy_available):
    nonce = web3.eth.getTransactionCount(my_address)
    txn = contract.functions.registerEnergy(energy_available).buildTransaction({
        'chainId': 3,  # Ropsten network
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = web3.eth.account.signTransaction(txn, private_key=private_key)
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f'Transaction sent: {web3.toHex(txn_hash)}')

# Trade energy
def trade_energy(seller, amount):
    nonce = web3.eth.getTransactionCount(my_address)
    txn = contract.functions.tradeEnergy(seller, amount).buildTransaction({
        'chainId': 3,
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = web3.eth.account.signTransaction(txn, private_key=private_key)
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f'Transaction sent: {web3.toHex(txn_hash)}')

# Get available energy
def get_available_energy(producer):
    available_energy = contract.functions.getAvailableEnergy(producer).call()
    print(f'Available energy for {producer}: {available_energy} kWh')

# Example usage
register_energy(100)  # Register 100 kWh of energy
# Replace 'SELLER_ADDRESS' with the actual seller's address before running this
# trade_energy('SELLER_ADDRESS', 10)  # Trade 10 kWh of energy
# get_available_energy(my_address)  # Get available energy for your address
