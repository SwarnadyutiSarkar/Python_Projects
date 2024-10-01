import hashlib
import json
from time import time
from flask import Flask, request, jsonify

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def to_dict(self):
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data,
            'hash': self.hash
        }

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_records = []
        self.create_block(previous_hash='1')  # Create the genesis block

    def create_block(self, previous_hash):
        block = Block(
            index=len(self.chain) + 1,
            previous_hash=previous_hash,
            timestamp=time(),
            data=self.current_records,
            hash=self.hash_block(previous_hash)
        )
        self.current_records = []  # Reset current records
        self.chain.append(block)
        return block

    def hash_block(self, previous_hash):
        block_string = json.dumps(self.current_records, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_record(self, patient_id, record):
        self.current_records.append({
            'patient_id': patient_id,
            'record': record
        })
        return self.create_block(previous_hash=self.chain[-1].hash)

    def get_chain(self):
        return [block.to_dict() for block in self.chain]

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/add_record', methods=['POST'])
def add_record():
    data = request.get_json()
    patient_id = data.get('patient_id')
    record = data.get('record')

    if not patient_id or not record:
        return jsonify({'error': 'Patient ID and record are required'}), 400

    block = blockchain.add_record(patient_id, record)
    return jsonify({
        'message': 'Record added',
        'block': block.to_dict()
    }), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify(blockchain.get_chain()), 200

if __name__ == '__main__':
    app.run(debug=True)
