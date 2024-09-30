# storage/leveldb_storage.py
import plyvel

db = plyvel.DB('./blockchain.db', create_if_missing=True)

def store_data(key, value):
    """Stores data in LevelDB."""
    db.put(key.encode(), value.encode())

def retrieve_data(key):
    """Retrieves data from LevelDB."""
    return db.get(key.encode())
