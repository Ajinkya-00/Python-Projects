from emp import Emp

class HR(Emp):
    def __init__(self, id, name, basic, comm):
        super().__init__(id, name, basic)
        self.comm = comm
        self.dept = "HR"
        self.other = comm

    def calsal(self):
        da_amt = self.basic * 0.1
        hra_amt = self.basic * 0.12
        self.total = self.basic + da_amt + hra_amt + self.comm
        return self.total
