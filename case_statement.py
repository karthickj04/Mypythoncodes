import sys

values = sys.argv
bal = 10000
match values[1]:
    case "1":
        print("Your account balance is ", bal)
    case "2":
        wd = int(input("Enter the amount you want to withdraw"))
        bal1 = bal - wd
        print("Your Account Balance is ", bal1)
    case "3":
        dp = int(input("Enter the amount you want to deposit:"))
        bal2 = bal + dp
        print("Your Account Balance is ", bal2)
    case _:
        print("Please choose valid choice between 1,2,3:")