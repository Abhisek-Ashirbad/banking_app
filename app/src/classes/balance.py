from src.db.models.balance_db import BalanceDB

class Balance:
    def __init__(self, acc_id):
        self.acc_id = acc_id

    def deposit(self, amount):
        """Deposit an amount to the balance"""
        if amount <= 0:
            return False
        BalanceDB.update_balance(self.acc_id, amount)
        return True

    def display_balance(self):
        return BalanceDB.get_balance(self.acc_id)

    def withdraw(self, amount):
        """Withdraw an amount from the balance"""
        if amount <= 0:
            return False
        current_balance = self.display_balance()
        if current_balance >= amount:
            BalanceDB.update_balance(self.acc_id, -amount)  # Use negative amount for withdrawal
            return True
        return False
