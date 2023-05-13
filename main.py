from hashlib import sha256
import time
NONCE_LIMIT =100000000
difficulty = 3
tx = sha256(b"transactions_are_here").hexdigest()
last_block = sha256(b"Last_block").hexdigest()
print(tx)
def mine(block_height, last_block, tx, nonce, difficulty):
    for nonce in range(NONCE_LIMIT):
        base = str(block_height) + last_hash+ tx + str(nonce)
        calc_digest = sha256(base.encode()).hexdigest()
        




