class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.peers = []

    def add_peer(self, peer):
        """Adds a new peer to the network."""
        self.peers.append(peer)
        print(f"Peer {peer} added to the node {self.node_id}.")
