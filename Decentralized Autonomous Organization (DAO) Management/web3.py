from web3 import Web3
import json

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('https://your-infura-or-node-url'))

# Load your contract ABI and address
with open('SimpleDAOABI.json') as f:
    abi = json.load(f)

contract_address = '0xYourContractAddress'
dao_contract = w3.eth.contract(address=contract_address, abi=abi)

# Function to join the DAO
def join_dao(private_key, account):
    tx = dao_contract.functions.joinDAO().buildTransaction({
        'from': account,
        'nonce': w3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Function to create a proposal
def create_proposal(description, private_key, account):
    tx = dao_contract.functions.createProposal(description).buildTransaction({
        'from': account,
        'nonce': w3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Function to vote on a proposal
def vote_on_proposal(proposal_id, private_key, account):
    tx = dao_contract.functions.vote(proposal_id).buildTransaction({
        'from': account,
        'nonce': w3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Function to execute a proposal
def execute_proposal(proposal_id, private_key, account):
    tx = dao_contract.functions.executeProposal(proposal_id).buildTransaction({
        'from': account,
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

    # Join the DAO
    join_tx_hash = join_dao(private_key, account)
    print(f"Joined DAO: {join_tx_hash.hex()}")

    # Create a proposal
    proposal_tx_hash = create_proposal("Increase funding for Project X", private_key, account)
    print(f"Proposal created: {proposal_tx_hash.hex()}")

    # Vote on a proposal (assuming proposal ID is 0)
    vote_tx_hash = vote_on_proposal(0, private_key, account)
    print(f"Voted on proposal: {vote_tx_hash.hex()}")

    # Execute the proposal (if enough votes)
    execute_tx_hash = execute_proposal(0, private_key, account)
    print(f"Executed proposal: {execute_tx_hash.hex()}")
