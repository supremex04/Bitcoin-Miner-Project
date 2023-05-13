from hashlib import sha256
import time
NONCE_LIMIT =100000000
block_height =0
difficulty = 3
tx = sha256(b"transactions_are_here").hexdigest()
last_block = sha256(b"Last_block").hexdigest()
def mine(block_height, last_block, tx,difficulty):
    for nonce in range(NONCE_LIMIT):
        base = str(block_height) + last_block+ tx + str(nonce)
        calc_digest = sha256(base.encode()).hexdigest()
        if calc_digest.startswith("0"*difficulty):
            print(f"Block mined: {calc_digest} \nNonce is: {nonce}")
            return nonce
        
mine(block_height, last_block, tx, difficulty)



