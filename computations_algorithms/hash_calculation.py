import hashlib

def calculate_hash(data):
    """Calculates the SHA-256 hash of the given data."""
    return hashlib.sha256(data.encode()).hexdigest()
