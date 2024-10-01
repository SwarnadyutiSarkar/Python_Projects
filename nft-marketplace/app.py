# app.py

from flask import Flask, request, jsonify
from web3 import Web3
import json

app = Flask(__name__)

# Connect to local Ethereum node (or a testnet)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  # Adjust if needed

# Load the contract
with open('ArtNFT.json') as f:
    contract_data = json.load(f)

contract_address = 'YOUR_CONTRACT_ADDRESS'  # Replace with your contract address
contract = w3.eth.contract(address=contract_address, abi=contract_data['abi'])

# Replace with your wallet address
wallet_address = 'YOUR_WALLET_ADDRESS'  # Replace with your wallet address

@app.route('/mint', methods=['POST'])
def mint_nft():
    token_uri = request.json['tokenURI']
    nonce = w3.eth.getTransactionCount(wallet_address)

    # Create transaction
    txn = contract.functions.mint(token_uri).buildTransaction({
        'chainId': 1,  # Mainnet, change to 4 for Rinkeby
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'nonce': nonce,
    })

    # Sign transaction
    signed_txn = w3.eth.account.sign_transaction(txn, private_key='YOUR_PRIVATE_KEY')  # Replace with your private key
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    return jsonify({'transaction_hash': txn_hash.hex()})


@app.route('/tokenURI/<int:token_id>', methods=['GET'])
def get_token_uri(token_id):
    uri = contract.functions.tokenURI(token_id).call()
    return jsonify({'tokenURI': uri})

if __name__ == '__main__':
    app.run(debug=True)
