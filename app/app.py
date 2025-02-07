import typer
from src.classes.account import Account
from src.classes.balance import Balance
from src.db.models.account_db import AccountDB
from src.db.models.balance_db import BalanceDB

app = typer.Typer()

def run_menu():
    """Run the interactive menu interface"""
    AccountDB.initialize_db()  # Ensures 'account' table creation
    BalanceDB.initialize_db()  # Ensures 'balances' table is created

    while True:
        print("""
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
        """)
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Enter Username: ")
            acc_type = input("Enter Account Type: ")
            address = input("Enter Address: ")
            branch = input("Enter Branch: ")
            create_account(username, acc_type, address, branch)
        
        elif choice == "2":
            acc_id = int(input("Enter Account ID: "))
            username = input("Enter new Username (leave blank to keep unchanged): ") or None
            acc_type = input("Enter new Account Type (leave blank to keep unchanged): ") or None
            address = input("Enter new Address (leave blank to keep unchanged): ") or None
            branch = input("Enter new Branch (leave blank to keep unchanged): ") or None
            update_account(acc_id, username, acc_type, address, branch)
        
        elif choice == "3":
            acc_id = int(input("Enter Account ID: "))
            delete_account(acc_id)
        
        elif choice == "4":
            acc_id = int(input("Enter Account ID: "))
            amount = float(input("Enter amount to deposit: "))
            deposit(acc_id, amount)
        
        elif choice == "5":
            acc_id = int(input("Enter Account ID: "))
            display_balance(acc_id)
        
        elif choice == "6":
            acc_id = int(input("Enter Account ID: "))
            amount = float(input("Enter amount to withdraw: "))
            withdraw(acc_id, amount)
        
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

@app.command(name="menu", help="List the interactive banking menu")
def menu():
    """Run the interactive banking menu"""
    run_menu()

@app.command(name="create-account")
def create_account(
    username: str = typer.Option(..., "--username", "-u", help="Username"),
    acc_type: str = typer.Option(..., "--type", "-t", help="Account Type"),
    address: str = typer.Option(..., "--address", "-a", help="Address"),
    branch: str = typer.Option(..., "--branch", "-b", help="Branch")
):
    account = Account(username, acc_type, address, branch)
    account.create()
    typer.echo(f"Account created for {username}")

@app.command(name="update-account")
def update_account(
    acc_id: int = typer.Option(..., "--id", help="Account ID"),
    username: str = typer.Option(None, "--username", "-u", help="New Username"),
    acc_type: str = typer.Option(None, "--type", "-t", help="New Account Type"),
    address: str = typer.Option(None, "--address", "-a", help="New Address"),
    branch: str = typer.Option(None, "--branch", "-b", help="New Branch")
):
    account = Account.get_by_id(acc_id)
    if account:
        account.update(username, acc_type, address, branch)
        typer.echo("Account updated successfully.")
    else:
        typer.echo("Account not found.")

@app.command(name="delete-account")
def delete_account(
    acc_id: int = typer.Option(..., "--id", help="Account ID")
):
    account = AccountDB.get(acc_id)
    if account:
        AccountDB.delete(acc_id)
        typer.echo(f"Account {acc_id} deleted successfully.")
    else:
        typer.echo(f"Account {acc_id} not found.")

@app.command(name="deposit")
def deposit(
    acc_id: int = typer.Option(..., "--id", help="Account ID"),
    amount: float = typer.Option(..., "--amount", "-a", help="Amount to deposit")
):
    balance = Balance(acc_id)
    balance.deposit(amount)
    typer.echo(f"Deposited {amount} to account {acc_id}")

@app.command(name="balance")
def display_balance(
    acc_id: int = typer.Option(..., "--id", help="Account ID")
):
    balance = Balance(acc_id)
    amt = balance.display_balance()
    typer.echo(f"Balance for account {acc_id}: {amt}")

@app.command(name="withdraw")
def withdraw(
    acc_id: int = typer.Option(..., "--id", help="Account ID"),
    amount: float = typer.Option(..., "--amount", "-a", help="Amount to withdraw")
):
    balance = Balance(acc_id)
    success = balance.withdraw(amount)
    if success:
        typer.echo(f"Withdrew {amount} from account {acc_id}")
    else:
        typer.echo("Insufficient funds or invalid amount.")

if __name__ == "__main__":
    app()