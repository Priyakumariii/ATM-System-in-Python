import datetime

# Class to represent an ATM
class ATM:
    def __init__(self):
        # Sample database of accounts (for simplicity, stored in a dictionary)
        # Format: {account_number: {'pin': pin, 'balance': balance, 'transaction_history': []}}
        self.accounts = {
            '1234567890': {'pin': '1234', 'balance': 5000.0, 'transaction_history': []}
        }

    def run(self):
        print("Welcome to the ATM")

        while True:
            print("\nPlease choose an option:")
            print("1. Account Balance Inquiry")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.withdraw_cash()
            elif choice == '3':
                self.deposit_cash()
            elif choice == '4':
                self.change_pin()
            elif choice == '5':
                self.show_transaction_history()
            elif choice == '6':
                print("Thank you for visiting our ATM Machine... See you Again!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

    def authenticate(self, account_number, pin):
        # Authenticates the account number and PIN
        if account_number in self.accounts and self.accounts[account_number]['pin'] == pin:
            return True
        else:
            return False

    def check_balance(self):
        # Checks and displays the account balance
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if self.authenticate(account_number, pin):
            balance = self.accounts[account_number]['balance']
            print(f"Your account balance is: ${balance:.2f}")

    def withdraw_cash(self):
        # Allows cash withdrawal from the account
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if self.authenticate(account_number, pin):
            balance = self.accounts[account_number]['balance']
            amount = float(input("Enter amount to withdraw: $"))

            if amount > balance:
                print("Insufficient funds")
            else:
                self.accounts[account_number]['balance'] -= amount
                transaction = (datetime.datetime.now(), 'Withdrawal', amount)
                self.accounts[account_number]['transaction_history'].append(transaction)
                print(f"Withdrawal successful. Remaining balance: ${self.accounts[account_number]['balance']:.2f}")

    def deposit_cash(self):
        # Allows cash deposit into the account
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if self.authenticate(account_number, pin):
            amount = float(input("Enter amount to deposit: $"))
            self.accounts[account_number]['balance'] += amount
            transaction = (datetime.datetime.now(), 'Deposit', amount)
            self.accounts[account_number]['transaction_history'].append(transaction)
            print(f"Deposit successful. New balance: ${self.accounts[account_number]['balance']:.2f}")

    def change_pin(self):
        # Allows changing the PIN of the account
        account_number = input("Enter your account number: ")
        pin = input("Enter your current PIN: ")

        if self.authenticate(account_number, pin):
            new_pin = input("Enter new PIN: ")
            self.accounts[account_number]['pin'] = new_pin
            print("PIN changed successfully")

    def show_transaction_history(self):
        # Displays transaction history for the account
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if self.authenticate(account_number, pin):
            history = self.accounts[account_number]['transaction_history']
            if not history:
                print("No transactions yet.")
            else:
                print("Transaction History:")
                for transaction in history:
                    print(f"Date: {transaction[0]}, Type: {transaction[1]}, Amount: ${transaction[2]:.2f}")

# Main program entry point
if __name__ == "__main__":
    atm = ATM()
    atm.run()
