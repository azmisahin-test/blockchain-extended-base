class ProofOfAuthority:
    def __init__(self, validators):
        self.validators = validators

    def select_validator(self):
        """Selects a validator from a predefined list of validators."""
        return random.choice(self.validators)
