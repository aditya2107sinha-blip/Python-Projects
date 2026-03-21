import datetime
PIN = 2107
balance = 10000000

def ATM_inside(name):
    for attempts in range(3):
            pincode = int(input("please enter your Pincode"))
            if pincode.isdigit() and pincode == PIN:
                break
            print(F"YOU HAVE LEFT {2 - attempts} ATTEMPTS ONLY")
    while(True):
        print("**Welcome To Our ATM**")        
        print("What do you want to do \n1)Check Balance \n2)credit any amount \n3)withdraw an amount")

        choice = int(input("enter your choice"))
        if choice == 1:
            print(f"Your current balance is {balance}")
            print(f"{name} checked the balance on {datetime.date.today()}")

        elif choice == 2:
            for j in range(3):
                amount = int(input("enter the amount you want to credit:"))
                if not 0 < amount < 500000:
                    print("can't credit this amount")
                else:
                    balance+= amount
                    print(f"Your total balance is now {balance}")

                    print("Do you want to credit more?\n1)Yes\n2)No")
                    dicision = int(input("enter your dicision:"))
                    if dicision == 1:
                       continue
                    else:
                        break
                print(f"{name} credited {amount} on {datetime.date.today()}")

        elif choice == 3:
            withdarwing_amount = int(input("enter the amount you want to withdraw"))
            if withdarwing_amount > balance:
                print("Can't withdraw")

            else:
                balance -= withdarwing_amount
                print(balance - withdarwing_amount)

            print(f"{name} withdrew {withdarwing_amount} on {datetime.date.today()}")
            print("Do you want to do anything again?")
            option = int(input("enter your option: "))
            if option == 1:
                 continue
            else:
                 break

ATM_inside("Aditya")






