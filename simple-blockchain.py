from hashlib import sha256

import json

import time 

class Chain:

    def __init__(self):

        self.blockchain = []

        self.pending = []

        self.add_block(prevhash="Genesis", proof=123)

    def add_transaction(self, sender, recipient, amount):

        transaction = {

            "sender": sender,

            "recipient": recipient,

            "amount": amount

        }

        self.pending.append(transaction)

    def compute_hash(self, block):

        json_block = json.dumps(block, sort_keys=True).encode()

        curhash = sha256(json_block).hexdigest()

        return curhash

    def add_block(self, proof, prevhash=None):

        block = {

            "index": len(self.blockchain),

            "timestamp": time.time(),

            "transactions": self.pending,

            "proof": proof,

            "prevhash": prevhash or self.compute_hash(self.blockchain[-1])

        }

        self.pending = []

        self.blockchain.append(block)

chain = Chain()

t1 = chain.add_transaction("Shreyash", "Chauhan", 100)

t2 = chain.add_transaction("Sujal", "Samai", 10)

t3 = chain.add_transaction("Yash", "Sehgal", 34)

chain.add_block(12345)

t4 = chain.add_transaction("Uttam", "Singh", 23)

t5 = chain.add_transaction("Tejas", "Shah", 3)

t6 = chain.add_transaction("Nishant", "Jain", 88)

chain.add_block(6789)

print(chain.blockchain)
