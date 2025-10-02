from emp import Emp

class Dev(Emp):
    def __init__(self, id, name, basic, bonus):
        super().__init__(id, name, basic)
        self.bonus = bonus
        self.dept = "Android"
        self.other = bonus

    def calsal(self):
        da_amt = self.basic * 0.1
        hra_amt = self.basic * 0.12
        self.total = self.basic + da_amt + hra_amt + self.bonus
        return self.total
