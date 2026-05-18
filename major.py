import random

def Bank_management_system():
    while(True):
        choice = (input("Enter the number of option you want:\n1.Create a account\n2.User login\n3.Admin login\n4.Exit\n"))
        if choice == "1" and choice.isdigit():
            print("Please fill the details:")
            Name = str(input("Please enter your name: "))

            age = int(input("PLease enter your valid age: "))
            if not 18<age<100:
                print("Must be 18+ to create an account..")
                return
            initial_deposit = int(input("How much do you want to deposit as initial deposit?: "))
            if initial_deposit < 3000:
                print("Atleast it should be 3000..")
                return
            elif initial_deposit>500000:
                print("Initially this amount can't be deposited")
                return
            password = ""
            for i in range(1,12):
                num = random.randint(1,10)
                password += str(num)
            default_PIN = int(input("Create a default PIN"))
            confirm_PIN = int(input("Confirm your default PIN"))
            if default_PIN == confirm_PIN:
                print("Your PIN is confirmed")

            print("!!!!!Your Account is succesfully generated!!!!!\nAll the details are in Your_new_account.txt file")

            with open("Your_new_account.txt","a") as ync:
                ync.write(f"{Name},{age},{confirm_PIN},{password},{initial_deposit}\n")

        if choice == "2" and choice.isdigit():
            
            check_acc_num = int(input("Enter your account number: "))
            with open("Your_new_account.txt","r") as ync:
                    for i in ync.readlines():
                        data = i.strip().split(",")
                        # print(data)
                        if data[3] == str(check_acc_num):
                            print("Account Found!!")
                            break
                    else:
                        print("Account Not found!!")
                        return    
            for j in range(3):
                chance = j
                ASK_PIN = int(input("Enter the PIN: "))
                if str(ASK_PIN) == data[2]:
                    print("Successfull!!")
                    break
                else:
                        print("Wrong PIN try again..")
                        print(f"You have {(2-chance)} Chances")

            else:
                print("You Entered wrong PIN")
                return      
            while(True):        
                print("**User Menu**\n1)Check balance\n2)Deposit\n3)Withdraw\n4)Transfer to another person\n5)Transaction History\n6)Change PIN\n7)Log Out\n")
                choice = int(input("Enter your choice:"))
                if choice == 1:
                    Who_you_are = input("Enter your name as per your account:")
                    with open("Your_new_account.txt","r") as ync:
                        for _ in ync.readlines():
                            data_2 = _.strip().split(",")
                            if str(Who_you_are) == data_2[0]:
                                print("User verified")
                                break
                        print(f"Your current balance is {data_2[4]}")
                    with open("Transaction.txt","a") as t:
                        t.write(f"{Who_you_are} Checked balance and the total Balance is {data_2[4]}\n")
                    

                if choice == 2:
                    print("You are depositing money:")
                    Who_you_are2 = input("Enter your name as per your account:")
                    with open("Your_new_account.txt","r") as ync:
                            for _ in ync.readlines():
                                data_3 = _.strip().split(",")
                                if str(Who_you_are2) == data_3[0]:
                                    print("User verified")
                                    break
                            else:
                                print("This name is not registered!!")
                                return
                    how_much = int(input("Enter the amount of money you want to deposit:"))
                    with open("Your_new_account.txt","r") as ync:
                            balance = ync.read()

                    total_balance = how_much+int(data_3[4])
                    new_balance = balance.replace(str(data_3[4]),str(total_balance))

                    with open("Your_new_account.txt","w") as ync:
                            ync.write(new_balance)
                            print(f"{how_much} is deposited to your bank account\nYour current balance is {total_balance}")
                    
                    with open("Transaction.txt","a") as t:
                        t.write(f"{Who_you_are2} deposited {how_much} and the total balance is {total_balance}\n")
                
                if choice == 3:      
                    Who_you_are3 = input("Enter your name as per your account:").strip()

                    with open("Your_new_account.txt","r") as ync:
                            for i in ync.readlines():
                                data_4 = i.strip().split(",")
                                if str(Who_you_are3) == data_4[0]:
                                    print("User Verified!")
                                    break
                            else:
                                print("This user is not registered!")
                                return
                    how_much2 = int(input("Enter the amount you want to withdraw:"))
                    with open("Your_new_account.txt","r") as ync:
                        for line in ync.readlines():
                            check = line.strip().split(",")
                            if int(check[4]) <=0:
                                print("Invalid amount")
                                break
                            elif int(check[4]) == how_much2:
                                print("!!Something went wrong!!")
                                break
                            elif how_much2 > int(check[4]):
                                print("ERROR")
                                break
                        else:
                            with open("Your_new_account.txt","r") as file:
                                    upadating = file.read()
                            withdraw = int(check[4]) - how_much2
                        
                            new_upadating = upadating.replace(str(check[4]),str(withdraw))
                            with open("Your_new_account.txt","w") as file:
                                    file.write(new_upadating)
                            print(f"{how_much2} is withdrawed and\n{str(withdraw)} left")

                            with open("Transaction.txt","a") as t:
                                t.write(f"{Who_you_are3} withdrawed {how_much2} and the total balance is {withdraw}\n")
                if choice == 4:
                    print("You are transfering money:")
                    Who_you_are4 = input("Enter your name as per your account:")
                    how_much3 = int(input("Enter the amount of money to want to transfer:"))
                    with open("Your_new_account.txt","r") as ync:
                        all_lines = ync.readlines()
                        for k in all_lines:
                            data_5 = k.strip().split(",")
                            if str(Who_you_are4)== data_5[0]:
                                print("User verified")
                                if how_much3 <= int(data_5[4]):
                                    Remaining = int(data_5[4]) - how_much3
                                elif how_much3 > int(data_5[4]):
                                    print("Insufficient balance!!")
                                else:
                                    print("Something went wrong!")
                                break
                        else:
                            print("This user is not registerd")
                            return
                        to_whom = input("Enter the name of the person you want to transfer money:")
                        for h in all_lines:
                            for_this = h.strip().split(",")
                            if to_whom == for_this[0]:
                                print("The user you are transfering money is also verified")
                                added = int(for_this[4]) + how_much3
                                break
                        else:
                            print("Nahi h aisa koi")
                            return
                    with open("Your_new_account.txt","r") as ync:
                        checking = ync.read()
                    new_checking = checking.replace(str(data_5[4]),str(Remaining))
                    new_checking = new_checking.replace(str(for_this[4]),str(added))
                    with open("Your_new_account.txt","w") as ync:
                        ync.write(new_checking)
                        print(f"You transfered {how_much3} to {to_whom}\nYour remaining balance is {Remaining}")
                    with open("Transaction.txt","a") as t:
                                t.write(f"{Who_you_are4} transfered {how_much3} to {to_whom}\n")
                if choice == 5:
                    acc_num = int(input("Enter your account number:"))
                    with open("Your_new_account.txt","r") as ync:
                        for i in ync.readlines():
                            data_new = i.strip().split(",")
                            if str(acc_num) == data_new[3]:
                                print("User found!!")
                                break
                        else:
                            print("No such user found")
                            break
                    print("Your transaction history:-")
                    with open("Transaction.txt","r") as t:
                        print(t.read())
                if choice == 6:
                    ask = input("Do you want to change password?(y/n)")
                    if ask == "y":
                        asking = int(input("Enter your account number:"))
                        with open("Your_new_account.txt","r") as ync:
                            for i in ync.readlines():
                                data_newish = i.strip().split(",")
                                if str(asking) == data_newish[3]:
                                    print("User verified!!")
                                    break
                            else:
                                print("User not found!!")
                                return
                        change = int(input("Enter your new PIN code: "))
                        with open("Your_new_account.txt","r") as fi:
                            let = fi.read()

                        now_let = let.replace(str(data_newish[2]),str(change))

                        with open("Your_new_account.txt","w") as fi:
                            fi.write(now_let)
                            print(f"You changed Your PIN code and new PIN code is {change}")
                             
                if choice == 7:
                    print("You are logging Out....")
                    print("Do you want to do anything else:-")
                    break
                        
        if choice == "3" and choice.isdigit():
            print("WELCOME ADMIN!")
            admin_pass = input("Enter admin password:")
            while(True):
                if admin_pass == "Aditya123":  
                    print("Admin Menu :-\n1)View all accounts\n2)Search account\n3)Delete account\n4)View all transaction\n5)Exit")
                    choose = int(input("Enter your choice:-"))
                    if choose == 1:
                        print("All accounts:-")
                        with open("Your_new_account.txt","r") as ync:
                            print(ync.read())
                    
                    if choose == 2:
                        whos_account = input("Who's account you are searching for admin?")
                        with open("Your_new_account.txt","r") as ync:
                            for i in ync.readlines():
                                admin_data = i.strip().split(",")
                                if whos_account == admin_data[0]:
                                    print("Account found!")
                                    print(f"Here are the details\n{i}")
                    if choose == 3:
                        whos_account_delete = input("Enter the name of person who's account you want to delete:-")
                        with open("Your_new_account.txt","r") as ync:
                            alllines = ync.readlines()

                        for line in alllines :
                            if whos_account_delete in line:
                                print("User Found!!")
                                tell = input("Really want to delete this account(y/n):")
                                if tell == "y":
                                    alllines.remove(line)
                                    with open("Your_new_account.txt","w") as ync:
                                        ync.writelines(alllines)
                                    print("Account deleted!!")
                                    break
                        else:
                            print("Something went wrong!!")
                    if choose == 4:
                        with open("Transaction.txt","r") as ync:
                            print(ync.read())
                    if choose == 5:
                        print("Thankyou admin!!")
                        print("Do you want to do anything else?...")
                        break
        if choice == "4" and choice.isdigit():
            print("Thankyou!!...")
            break

Bank_management_system()
