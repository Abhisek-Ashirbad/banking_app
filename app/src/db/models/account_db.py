import sqlite3

class AccountDB:
    @staticmethod
    def initialize_db():
        """Create the accounts table if it doesn't exist"""
        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                acc_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                acc_type TEXT NOT NULL,
                address TEXT NOT NULL,
                branch TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def insert(username, acc_type, address, branch):
        """Insert a new account into the database"""
        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO accounts (username, acc_type, address, branch) VALUES (?, ?, ?, ?)", 
                    (username, acc_type, address, branch))
        acc_id = cur.lastrowid  # Get the newly created account ID
        conn.commit()
        conn.close()
        return acc_id  # Return the new account ID

    @staticmethod
    def get(acc_id):
        """Retrieve account details by account ID"""
        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM accounts WHERE acc_id=?", (acc_id,))
        result = cur.fetchone()
        conn.close()
        return result  # Returns None if the account doesn't exist

    @staticmethod
    def delete(acc_id):
        """Delete an account by ID"""
        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM accounts WHERE acc_id=?", (acc_id,))
        conn.commit()
        conn.close()
