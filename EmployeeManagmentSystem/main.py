from empManage import EmpManage

def login():
    user = "admin"
    password = "1234"

    userId = input("Enter User Id: ")
    passw = input("Enter Password: ")

    if userId == user and passw == password:
        print("Login Successfully!")
        em = EmpManage()   

        ch = '0'
        while ch != "6":
            print("\n===== Employee Management System =====")
            print("1. Add Employee")
            print("2. Update Employee")
            print("3. Delete Employee")
            print("4. Show All Employees")
            print("5. Search Employee")
            print("6. Exit")

            ch = input("Enter your choice: ")

            if ch == '1':
                em.addEmp()
            elif ch == '2':
                em.updEmp()
            elif ch == '3':
                em.delEmp()
            elif ch == '4':
                em.showAllEmp()
            elif ch == '5':
                em.searchEmp()
            elif ch == '6':
                print("Exited successfully..")
            else:
                print("Invalid choice...")
    else:
        print("Invalid login!")


ch = '0'
while ch != '2':
    print('''\nPlease select your choice
1. Login
2. Exit''')
    ch = input("Enter your choice: ")

    if ch == '1':
        login()
    elif ch == '2':
        print("Exited successfully.")
    else:
        print("Invalid choice.")