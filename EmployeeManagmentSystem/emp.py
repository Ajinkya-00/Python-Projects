class Emp:
    def __init__(self, id, name, basic):
        self.id = id
        self.name = name
        self.basic = basic
        self.total = 0
        self.dept = ""
        self.other = 0

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Basic: {self.basic}, Department: {self.dept}, Other: {self.other}, Total: {self.total}"
