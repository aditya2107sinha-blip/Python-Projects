import random

guide = {"rock":"R",
         "paper":"P",
         "scissor":"S"}
                       

you= input("enter your choice:").lower()
your_choice = guide[you]
print(f"you choose {your_choice}")
computer_choice = random.choice(["R","P","S"])
print(f"computer choose {computer_choice}")

if(your_choice==computer_choice):
    print("OHHH ITS A DRAW")

else:
    if(your_choice=="R" and computer_choice=="P"):
        print(f"YOU LOSE {computer_choice}")
    elif(your_choice=="R" and computer_choice=="S"):
        print(f"YOU WIN {your_choice}")
    elif(your_choice=="P" and computer_choice=="S"):
        print(f"YOU LOSE {computer_choice}")
    elif(your_choice=="P" and computer_choice=="R"):
        print(f"YOU WIN {your_choice}")
    elif(your_choice=="S" and computer_choice=="P"):
        print(f"YOU WIN {your_choice}")
    elif(your_choice=="S" and computer_choice=="R"):
        print(f"YOU LOSE {computer_choice}")