from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    """Generates a key for encryption."""
    return Fernet.generate_key()

# Encrypt data
def encrypt_message(key, message):
    """Encrypts a message using the provided key."""
    f = Fernet(key)
    return f.encrypt(message.encode())

# Decrypt data
def decrypt_message(key, encrypted_message):
    """Decrypts an encrypted message using the provided key."""
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()
