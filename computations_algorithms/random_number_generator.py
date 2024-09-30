import random

def generate_random_number(seed=None):
    """Generates a random number, optionally based on a seed."""
    if seed:
        random.seed(seed)
    return random.randint(1, 1000000)
