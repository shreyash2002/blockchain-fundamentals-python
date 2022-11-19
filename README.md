# blockchain-fundamentals-python

This is a simple program to create our own blockchain

We’ll need to import following libraries to start out -

<break>
sha256 : The sha256 function will give us the ability to compute hashes.<break>
json : We want JSON for parsing our data <break>
time : It is used for timestamping.<break>


You may ask 👇
What is a blockchain?

A blockchain is a ledger of “blocks” and blocks are a collection of transactions. Each block in the blockchain is linked to its predecessor.


We’ll create a class that will represent our entire blockchain.

When we’re adding transactions to the blockchain, what we’re really doing is just to add it to the list of pending transactions and then after a few transactions have been added, we wrap them up in a block and put it on the blockchain. For example: Alice sends Bob 100 BTC, Charlie sends Alice 5 BTC and Bob sends Eve 45 BTC; all three of these transactions are added to the list of pending transactions (which will then be put in a block). A transaction will be marked as approved only after it has been added to a block.

The transaction will be a dictionary containing the name of the sender, recipient, and the amount to be sent.

A hash is a fingerprint of some data. For example, if we pass “hello, world” to SHA-256 (a hashing algorithm), we might get something like 0xd34db33f. Since no two blocks will have the exact same transactions, we can use SHA-256 to create a unique identifier for the block. From now on, we can reference a certain block by using this ID called block hash.


We’re getting a JSON representation of the data in the block and returning the hash of the JSON block


The block dictionary stores the following:

index: The current index of the block in the blockchain (starting from 0).<break>
timestamp: The timestamp of when this block was added.<break>
transactions: The list of the pending transactions.<break>
proof: This is a number that is used to roughly verify the validity of a block. The process of finding this proof is known as “mining.” We have decided to leave out mining in our blockchain since it requires a lot of computing power.<break>
prevhash: This is the hash of the previous block in our blockchain. This is how we connect all the blocks in a chain, since each block just stores the hash of last.<break>


I made this program by using QuestBook https://openquest.xyz/ Tutorial.
