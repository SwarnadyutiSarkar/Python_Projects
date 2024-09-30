import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class DeFiLendingPlatform:
    def __init__(self):
        self.chain = []
        self.current_loans = []
        self.new_block(previous_hash='1', proof=100)  # Create the genesis block

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'loans': self.current_loans,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_loans = []  # Reset the current loans
        self.chain.append(block)
        return block

    def new_loan(self, loan_data):
        self.current_loans.append(loan_data)
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

# Create a DeFi Lending Platform instance
lending_platform = DeFiLendingPlatform()

@app.route('/request_loan', methods=['POST'])
def request_loan():
    data = request.get_json()
    loan_data = {
        'borrower': data.get('borrower'),
        'amount': data.get('amount'),
        'interest_rate': data.get('interest_rate'),
        'duration': data.get('duration'),  # in days
    }

    if not all(loan_data.values()):
        return jsonify({'message': 'All loan fields are required!'}), 400

    lending_platform.new_loan(loan_data)
    return jsonify({'message': 'Loan request has been recorded.'}), 201

@app.route('/mine', methods=['GET'])
def mine():
    last_block = lending_platform.last_block
    proof = 100  # Simplified proof of work
    previous_hash = lending_platform.hash(last_block)
    block = lending_platform.new_block(proof, previous_hash)

    response = {
        'message': 'New block mined!',
        'index': block['index'],
        'loans': block['loans'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': lending_platform.chain,
        'length': len(lending_platform.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
