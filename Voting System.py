import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_votes = []
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'votes': self.current_votes,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_votes = []  # Reset the current votes
        self.chain.append(block)
        return block

    def new_vote(self, candidate):
        self.current_votes.append(candidate)
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

# Create a Blockchain instance
voting_blockchain = Blockchain()

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    candidate = data.get('candidate')

    if not candidate:
        return jsonify({'message': 'Candidate not provided!'}), 400

    voting_blockchain.new_vote(candidate)
    return jsonify({'message': f'Vote for {candidate} has been recorded.'}), 201

@app.route('/mine', methods=['GET'])
def mine():
    last_block = voting_blockchain.last_block
    proof = 100  # Simplified proof of work, replace with a real algorithm
    previous_hash = voting_blockchain.hash(last_block)
    block = voting_blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'New block mined!',
        'index': block['index'],
        'votes': block['votes'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': voting_blockchain.chain,
        'length': len(voting_blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
