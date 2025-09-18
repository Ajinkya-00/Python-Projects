from savingAccount import SavingAccount
from currentAccount import CurrentAccount

print("Welcome to SBI Bank")
print("1. Saving Account")
print("2. Current Account")

choice = int(input("Choose account type : "))

if choice == 1:
    acc = SavingAccount(101, "Ajinkya", 1000)
elif choice == 2:
    acc = CurrentAccount(102, "Ajinkya", 2000)
else:
    print("Invalid choice!")
    exit()


while True:
    print("\n-----MENU-----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    op = int(input("Enter choice : "))

    if op == 1:
        amt = float(input("Enter amount to deposit : "))
        acc.deposit(amt)
    elif op == 2:
        amt = float(input("Enter amount to withdraw : "))
        acc.withdraw(amt)
    elif op == 3:
        acc.check_balance()
    elif op == 4:
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid option! Try again.")