def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def claculator():
    while True:
        print("\nOperations : +  -  *  /  ^  fact  exit")
        op = input("Enter your choice : ")

        if op == "exit":
            print("Calculator closed")
            break

        if op == "fact":
            n = int(input("Enter the number :"))
            print("Result :",factorial(n))
        
        else:
            a = int(input("Enter the value of a : "))
            b = int(input("Enter the value of b : "))
        
        if op == "+":
            print("Result :",a + b)

        elif op == "-":
            print("Result :",a - b)
        
        elif op == "*":
            print("Result :",a * b)
        
        elif op == "/":
            if b == 0:
                print("Error ! Division by zero")
            else:
                print("Result =", a / b)
            
        elif op == "^":
            print("Result :",a ** b)
        
        else:
            print("Invalid choice !")

claculator()