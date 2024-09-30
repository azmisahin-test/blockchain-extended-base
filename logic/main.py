from blockchain.blockchain import Blockchain
from logic.transaction_logic import Transaction
from logic.user_interaction import get_user_input

def main():
    blockchain = Blockchain()

    while True:
        sender, receiver, amount = get_user_input()
        transaction = Transaction(sender, receiver, amount)
        new_block = blockchain.add_block(transaction.to_dict())
        print(f"New block added: {new_block.hash}")

if __name__ == "__main__":
    main()
