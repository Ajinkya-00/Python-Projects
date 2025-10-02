from dev import Dev
from hr import HR
from admin import Admin
from prettytable import PrettyTable

class EmpManage:
    emp_detail = {}

    @staticmethod
    def addEmp():
        id = input("Enter ID: ")
        nm = input("Enter Name: ")
        basic = float(input("Enter Basic Salary: "))

        print('''Please select department:
        1. Android Developer
        2. HR
        3. Admin''')
        ch = input("Enter the choice: ")

        if (ch == '1'):
            bonus = float(input("Enter the bonus: "))
            emp = Dev(id, nm, basic, bonus)
        elif (ch == '2'):
            comm = float(input("Enter the commission: "))
            emp = HR(id, nm, basic, comm)
        elif (ch == '3'):
            allowance = float(input("Enter the allowance: "))
            emp = Admin(id, nm, basic, allowance)
        else:
            print("Invalid department choice.")
            return

        emp.calsal()
        edata = str(emp)  
        EmpManage.emp_detail[id] = edata
        print("Employee added successfully!")

        
        EmpManage.displayTable([edata])

    @staticmethod
    def updEmp():
        id = input("Enter Employee ID to update: ")
        if (id in EmpManage.emp_detail):
            print("Re-enter details to update:")
            EmpManage.addEmp()  
        else:
            print("Employee not found.")

    @staticmethod
    def delEmp():
        id = input("Enter Employee ID to delete: ")
        if (id in EmpManage.emp_detail):
            del EmpManage.emp_detail[id]
            print("Employee deleted.")
        else:
            print("Employee not found.")

    @staticmethod
    def showAllEmp():
        if (not EmpManage.emp_detail):
            print("No employee records found.")
        else:
            EmpManage.displayTable(EmpManage.emp_detail.values())

    @staticmethod
    def searchEmp():
        id = input("Enter Employee ID to search: ")
        if (id in EmpManage.emp_detail):
            print("Employee Found:")
            EmpManage.displayTable([EmpManage.emp_detail[id]])
        else:
            print("Employee not found.")

    @staticmethod
    def displayTable(emp_list):
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Basic", "Dept", "Other", "Total Salary"]

        for emp_str in emp_list:
            parts = emp_str.split(", ")
            data = {}
            for part in parts:
                if ":" in part:
                    key, value = part.split(":", 1)
                    data[key.strip()] = value.strip()

            table.add_row([
                data.get('ID', ''),
                data.get('Name', ''),
                data.get('Basic', ''),
                data.get('Department', ''),
                data.get('Other', ''),
                data.get('Total', '')
            ])

        print(table)

