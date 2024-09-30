def get_user_input():
    """Simple function to get transaction details from the user."""
    sender = input("Enter sender address: ")
    receiver = input("Enter receiver address: ")
    amount = float(input("Enter amount to transfer: "))
    return sender, receiver, amount
