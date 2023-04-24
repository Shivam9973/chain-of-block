import hashlib
import datetime

class Block:
    def _init_(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        sha.update(hash_str.encode('utf-8'))

        return sha.hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calc_hash()

        print("Block mined:", self.hash)
