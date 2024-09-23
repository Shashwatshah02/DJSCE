import hashlib
import json

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", "2024-01-01 00:00:00", "Genesis Block", calculate_hash(0, "0", "2024-01-01 00:00:00", "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = "2024-01-01 00:00:00"  # For simplicity, using a static timestamp
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

def print_blockchain(blockchain):
    for block in blockchain:
        print(block)

def main():
    blockchain = [create_genesis_block()]

    # Adding four blocks to the blockchain
    for i in range(1, 4):
        new_block = create_new_block(blockchain[-1], f"Block {i}")
        blockchain.append(new_block)

    print_blockchain(blockchain)

if __name__ == "__main__":
    main()