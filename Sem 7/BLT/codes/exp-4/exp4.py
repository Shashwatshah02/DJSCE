import hashlib
import time

def calculate_hash(index, previous_hash, timestamp, data, nonce):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data) + str(nonce)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def proof_of_work(previous_hash, index, data, difficulty):
    nonce = 0
    timestamp = str(int(time.time()))
    prefix = '0' * difficulty
    while True:
        hash = calculate_hash(index, previous_hash, timestamp, data, nonce)
        if hash.startswith(prefix):
            return nonce, hash
        nonce += 1

def main():
    index = 1
    previous_hash = '0'  # For the genesis block, or replace with the hash of the previous block
    data = 'Some transaction data'
    difficulty = 7  # Number of leading zeros required in hash

    print("Starting Proof of Work...")
    start_time = time.time()
    nonce, hash = proof_of_work(previous_hash, index, data, difficulty)
    end_time = time.time()

    print(f"Proof of Work completed in {end_time - start_time:.2f} seconds")
    print(f"Nonce: {nonce}")
    print(f"Hash: {hash}")

if __name__ == "__main__":
    main()
