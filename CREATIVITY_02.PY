import random

def generator():
    long = int(input("how long password you want? "))
    if  long < 8:
        print("There should be minimum 8 character in you password")
        return
    else:
        if long > 64:
            choose = input("Do you want to make this big password:(Y/N)").capitalize()
            if choose == "Y":
                print("Okay you can proceed..")
            
            else:
                return
    
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*1234567890"
    actual_password = ""

    for i in range(long):
        password = random.choice(chars)
        actual_password += password


    print(f"Your password is {actual_password}") 


generator()