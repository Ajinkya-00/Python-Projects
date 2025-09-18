class Account:
    def __init__(self, acc_no, name, balance = 0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
  
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} deposited. New Balance = {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'{amount} withdrawn. Balance = {self.balance}')
        else:
            print("Insufficient balance!")
    
    def check_balance(self):
        print(f'Balance = {self.balance}')