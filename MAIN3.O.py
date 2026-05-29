# import random
# Computer_Choice = random.randint(1,100)


# #### bhai function ke ander function call ker sakta h tu but bhai function ke ander function define nhi ker sakta h tu ####


# def playagain():
#         play_again = input("Do you want to play again(y/n): ")

#         if play_again == "y":
#             Game()
#         else:
#             print("Okay then thanks for playing.......")
            



# def Game():
#     attempts = 0
#     max_attempts = 7
#     while(True):
#         Your_choice = int(input("Enter your chosen number:"))
#         print(f"{Your_choice} is your choice")
#         attempts+=1

#         # print(f"{Computer_Choice} is computers choice")

#         if Computer_Choice < Your_choice:
#             print("your number is larger")
#             print("please guess small\n")
#         elif Computer_Choice > Your_choice:
#             print("your number is smaller")
#             print("please guess larger\n")
#         else:
#             Computer_Choice == Your_choice
#             print("YOU WIN!!!!!\n")
#             playagain()
#             break
#         print(f"Attempts = {attempts}/{max_attempts}")
#         if attempts==max_attempts:
#             print(f"You LOSE!!!\nCorrect answer is {Computer_Choice}")
#             playagain()
#             break


# Game()

# for i in range(1,101):
#     if i%2 == 0:
#         print(i)


# f = 'aditya'
# g = f[::-1]

# print(g)

# for i in range(101):
#     inp = int(input("enter a number:"))

#     print(inp**2)

lst = [9,34,2,43,54,12,1]

lst.sort()

print(lst)