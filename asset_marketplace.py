import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class AssetMarketplace:
    def __init__(self):
        self.chain = []
        self.current_assets = []
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'assets': self.current_assets,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_assets = []  # Reset the current assets
        self.chain.append(block)
        return block

    def new_asset(self, asset_data):
        self.current_assets.append(asset_data)
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# Initialize the Flask application
app = Flask(__name__)

# Create a Marketplace instance
marketplace = AssetMarketplace()

@app.route('/list_asset', methods=['POST'])
def list_asset():
    data = request.get_json()
    asset_data = {
        'owner': data.get('owner'),
        'name': data.get('name'),
        'value': data.get('value'),
        'description': data.get('description'),
    }

    if not all(asset_data.values()):
        return jsonify({'message': 'All asset fields are required!'}), 400

    marketplace.new_asset(asset_data)
    return jsonify({'message': 'Asset has been listed.'}), 201

@app.route('/mine', methods=['GET'])
def mine():
    last_block = marketplace.last_block
    proof = 100  # Simplified proof of work
    previous_hash = marketplace.hash(last_block)
    block = marketplace.new_block(proof, previous_hash)

    response = {
        'message': 'New block mined!',
        'index': block['index'],
        'assets': block['assets'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': marketplace.chain,
        'length': len(marketplace.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
