import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create genesis block
        self.new_block()

    def new_block(self, proof, previous_hash = None):
        '''
        Creates a new block in the blockchain
        :param proof: <int> the proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        '''
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'prev_hash': previous_hash or self.hash(self.chain[-1])
        }
        # Reset current list of transactions

    def new_transations(self, sender, recipient, amount):
        '''
        Creates a new transaction to be added to the next mined block.
        :param sender: <str> Address of sender
        :param recipient: <str> address of recipient
        :param amount: Amount of transaction
        :return: Index of the block that will hold this transaction
        '''

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1
    @staticmethod
    def hash(block):
        # Hashes a block
        pass

    @property
    def last_block(self):
        # returns last block in chain
        pass

