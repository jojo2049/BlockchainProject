class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # generates new Block and adds to chain
        pass

    def new_transations(self):
        # adding new transaction to list of transacitons
        pass

    @staticmethod
    def hash(block):
        # Hashes a block
        pass

    @property
    def last_block(self):
        # returns last block in chain
        pass

