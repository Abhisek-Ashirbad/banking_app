import sqlite3

class BalanceDB:
    @staticmethod
    def initialize_db():
        """Create the balances table if it doesn't exist"""
        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS balances (
                acc_id INTEGER PRIMARY KEY,
                balance REAL NOT NULL DEFAULT 0,
                FOREIGN KEY(acc_id) REFERENCES accounts(acc_id) ON DELETE CASCADE
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def get_balance(acc_id):
        """Retrieve the current balance for an account"""
        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()
        cur.execute("SELECT balance FROM balances WHERE acc_id=?", (acc_id,))
        result = cur.fetchone()
        conn.close()
        return result[0] if result else 0  # Return balance or 0 if no record exists


    @staticmethod
    def update_balance(acc_id, amount):
        """Update the balance by adding or subtracting an amount"""
        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()

        # Check if account exists in the balances table
        cur.execute("SELECT balance FROM balances WHERE acc_id=?", (acc_id,))
        result = cur.fetchone()

        if result:  # If the account exists, update balance
            new_balance = result[0] + amount
            if new_balance >= 0:  # Ensure balance doesn't go negative
                cur.execute("UPDATE balances SET balance=? WHERE acc_id=?", (new_balance, acc_id))
                conn.commit()
                conn.close()
                return True
        else:  # If no balance record exists, insert a new one (only for positive amounts)
            if amount > 0:
                cur.execute("INSERT INTO balances (acc_id, balance) VALUES (?, ?)", (acc_id, amount))
                conn.commit()
                conn.close()
                return True
        
        conn.close()
        return False