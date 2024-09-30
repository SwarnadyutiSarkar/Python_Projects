import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class PropertyManagement:
    def __init__(self):
        self.chain = []
        self.current_properties = []
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'properties': self.current_properties,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_properties = []  # Reset the current properties
        self.chain.append(block)
        return block

    def new_property(self, property_data):
        self.current_properties.append(property_data)
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

# Create a Property Management instance
property_management = PropertyManagement()

@app.route('/add_property', methods=['POST'])
def add_property():
    data = request.get_json()
    property_data = {
        'owner': data.get('owner'),
        'location': data.get('location'),
        'price': data.get('price'),
        'description': data.get('description'),
    }

    if not all(property_data.values()):
        return jsonify({'message': 'All property fields are required!'}), 400

    property_management.new_property(property_data)
    return jsonify({'message': 'Property has been added.'}), 201

@app.route('/mine', methods=['GET'])
def mine():
    last_block = property_management.last_block
    proof = 100  # Simplified proof of work
    previous_hash = property_management.hash(last_block)
    block = property_management.new_block(proof, previous_hash)

    response = {
        'message': 'New block mined!',
        'index': block['index'],
        'properties': block['properties'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': property_management.chain,
        'length': len(property_management.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
