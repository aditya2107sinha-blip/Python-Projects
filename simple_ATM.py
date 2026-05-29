def ATM():
    current_balance=5000000000000000
    n=int(input("enter the PIN:"))

    if(n==12344321):
        print("the PIN is correct")
        print("what do you want to do \n1) check balance")
        print("2) withdrawl money")
        choice=int(input("enter the choice"))
        if choice==1:
            print(f"your balance is {current_balance}")
        elif choice==2:
            amount=int(input("enter the amount to withdrawl:"))
            if amount<=current_balance:
                print("you withdrawl was succesful💪💪")
                print("do you want to see rest of your balance")
                print("1) yes")
                print("2) no")
                choice2=int(input("enter you choice yo say yes or no"))
                if choice2==1:
                    print(current_balance - amount)
                elif choice2==2:
                    print("okay mt dekh mujhe kya🤣🤣🤣🤣🤣")
            elif amount>current_balance:
                print("insufficient balance")
            elif amount==current_balance:
                print("now you have zero balance")
                
    else:
        print("NIKAL YAHA SE BSDK🤬🤬")

ATM()
