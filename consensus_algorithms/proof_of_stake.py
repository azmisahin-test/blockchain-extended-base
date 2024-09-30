class ProofOfStake:
    def __init__(self, stakers):
        self.stakers = stakers

    def select_validator(self):
        """Selects a validator based on stake."""
        return max(self.stakers, key=self.stakers.get)  # Simplified POS selection based on max stake
