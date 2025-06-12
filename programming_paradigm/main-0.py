# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting with ₵100

    if len(sys.argv) < 2:
        print("Usage: python3 main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_parts = sys.argv[1].split(':')
    command = command_parts[0].lower()
    amount = float(command_parts[1]) if len(command_parts) > 1 else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ₵{amount:.2f}")
        account.display_balance()
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ₵{amount:.2f}")
        else:
            print("Insufficient funds.")
        account.display_balance()
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use deposit, withdraw, or display.")

if __name__ == "__main__":
    main()

