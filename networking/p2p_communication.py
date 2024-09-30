import socket

def send_message(peer, message):
    """Sends a message to a peer over a socket connection."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((peer, 5000))
        s.sendall(message.encode())
        print(f"Message sent to {peer}: {message}")
