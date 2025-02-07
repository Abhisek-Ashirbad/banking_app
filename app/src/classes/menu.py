import typer
from src.classes.account import Account
from src.classes.balance import Balance
from src.db.models.account_db import AccountDB
from src.db.models.balance_db import BalanceDB

class Menu:
    def __init__(self):
        self.initialize_databases()

    @staticmethod
    def initialize_databases():
        """Initialize all required databases"""
        AccountDB.initialize_db()
        BalanceDB.initialize_db()

    @staticmethod
    def display_menu():
        """Display the main menu options"""
        return """
        =======================     
        # Banking-Application #
        =======================
        1. Create Account 
        2. Update Account
        3. Delete Account
        4. Deposit Money
        5. Display Current Balance
        6. Withdraw Money
        7. Exit
        """

    def create_account_input(self):
        """Handle create account input and operation"""
        username = input("Enter Username: ")
        acc_type = input("Enter Account Type: ")
        address = input("Enter Address: ")
        branch = input("Enter Branch: ")
        account = Account(username, acc_type, address, branch)
        account.create()
        print(f"Account created for {username}")

    def update_account_input(self):
        """Handle update account input and operation"""
        acc_id = int(input("Enter Account ID: "))
        username = input("Enter new Username (leave blank to keep unchanged): ") or None
        acc_type = input("Enter new Account Type (leave blank to keep unchanged): ") or None
        address = input("Enter new Address (leave blank to keep unchanged): ") or None
        branch = input("Enter new Branch (leave blank to keep unchanged): ") or None
        
        account = Account.get_by_id(acc_id)
        if account:
            account.update(username, acc_type, address, branch)
            print("Account updated successfully.")
        else:
            print("Account not found.")

    def delete_account_input(self):
        """Handle delete account input and operation"""
        acc_id = int(input("Enter Account ID: "))
        account = AccountDB.get(acc_id)
        if account:
            AccountDB.delete(acc_id)
            print(f"Account {acc_id} deleted successfully.")
        else:
            print(f"Account {acc_id} not found.")

    def deposit_input(self):
        """Handle deposit input and operation"""
        acc_id = int(input("Enter Account ID: "))
        amount = float(input("Enter amount to deposit: "))
        balance = Balance(acc_id)
        balance.deposit(amount)
        print(f"Deposited {amount} to account {acc_id}")

    def display_balance_input(self):
        """Handle balance display input and operation"""
        acc_id = int(input("Enter Account ID: "))
        balance = Balance(acc_id)
        amt = balance.display_balance()
        print(f"Balance for account {acc_id}: {amt}")

    def withdraw_input(self):
        """Handle withdrawal input and operation"""
        acc_id = int(input("Enter Account ID: "))
        amount = float(input("Enter amount to withdraw: "))
        balance = Balance(acc_id)
        success = balance.withdraw(amount)
        if success:
            print(f"Withdrew {amount} from account {acc_id}")
        else:
            print("Insufficient funds or invalid amount.")

    def run(self):
        """Run the interactive menu interface"""
        while True:
            print(self.display_menu())
            choice = input("Enter your choice: ")
            
            try:
                if choice == "1":
                    self.create_account_input()
                elif choice == "2":
                    self.update_account_input()
                elif choice == "3":
                    self.delete_account_input()
                elif choice == "4":
                    self.deposit_input()
                elif choice == "5":
                    self.display_balance_input()
                elif choice == "6":
                    self.withdraw_input()
                elif choice == "7":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError as e:
                print(f"Invalid input: Please enter correct values. Error: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")