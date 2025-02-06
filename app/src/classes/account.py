

class Account():
    def __init__(self, username, acc_type, address, branch, acc_id):
        self.username = username
        self.acc_type = acc_type
        self.address = address
        self.branch = branch
        self.acc_id = acc_id        

    def update_account(self, username=None, acc_type=None, address=None, branch=None, acc_id=None):
        if username is not None:
            self.username = username
        if acc_type is not None:
            self.acc_type = acc_type
        if address is not None:
            self.address = address
        if branch is not None:
            self.branch = branch
        if acc_id is not None:
            self.acc_id = acc_id

    def delete_account(self):
        pass

