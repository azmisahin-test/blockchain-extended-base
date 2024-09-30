from blockchain.block import Block

class ProofOfWork:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def mine_block(self, block):
        """Performs proof of work mining by adjusting the nonce until the hash has enough leading zeros."""
        target = '0' * self.difficulty
        while block.hash[:self.difficulty] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()
        print(f"Block mined: {block.hash}")
