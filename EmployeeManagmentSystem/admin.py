from emp import Emp

class Admin(Emp):
    def __init__(self, id, name, basic, allowance):
        super().__init__(id, name, basic)
        self.allowance = allowance
        self.dept = "Admin"
        self.other = allowance

    def calsal(self):
        da_amt = self.basic * 0.1
        hra_amt = self.basic * 0.12
        self.total = self.basic + da_amt + hra_amt + self.allowance
        return self.total
