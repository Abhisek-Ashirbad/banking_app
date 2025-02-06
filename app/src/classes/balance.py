

class Balance:
    def __init__(self, balance_amt = 0):
        self.balance_amt = balance_amt

    def deposit(self, deposit_amt):
        self.balance_amt += deposit_amt  # balance_amt = balance_amt + deposit_amt

    def withdraw(self, withdrawal_amt):
        if withdrawal_amt > self.balance_amt:
            print("Insufficient balance")
        self.balance_amt -= withdrawal_amt  # balance_amt = balance_amt - withdrawal_amt

    def display_balance(self):
        print(f"Current balance: {self.balance_amt}")