from account import Account

class CurrentAccount(Account):
    def __init__(self, acc_no, name, balance = 0):
        super().__init__(acc_no, name, balance)
