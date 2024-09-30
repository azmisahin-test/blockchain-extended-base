import ipfshttpclient

client = ipfshttpclient.connect()

def store_data(data):
    """Stores data in IPFS and returns the IPFS hash."""
    result = client.add_str(data)
    return result
