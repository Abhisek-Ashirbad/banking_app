
from src.db.models.account_db import AccountDB

class Account:
    def __init__(self, username, acc_type, address, branch):
        self.username = username
        self.acc_type = acc_type
        self.address = address
        self.branch = branch

    def create(self):
        AccountDB.insert(self.username, self.acc_type, self.address, self.branch)

    @staticmethod
    def get_by_id(acc_id):
        return AccountDB.get(acc_id)

    def update(self, username=None, acc_type=None, address=None, branch=None):
        AccountDB.update(self.username, username, acc_type, address, branch)

    def delete(self):
        AccountDB.delete(self.username)
