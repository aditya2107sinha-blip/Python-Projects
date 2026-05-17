def Add():
    name = input("Enter the name of the student: ")
    roll_num = int(input("Enter the Roll.no. of the student:"))
    print("Student added successfully!!")
    with open("Report_card.txt","a") as rc:
        rc.write(f"{name},{roll_num}\n")

def Add_student_marks():
    whos_marks = input("Enter the name of the student who's are getting added:")
    print("Enter what you are adding and then add makrs--")
    what , *marks = input().split()
    marks = ",".join(marks)
    with open("Report_card.txt","r") as rc:
        all_lines = rc.readlines()
        for i in range(len(all_lines)):
            check = all_lines[i].strip().split(",")
            if check[0] == whos_marks:
                print("Student Found!!")
                all_lines[i] = f"{check[0]},{check[1]},{marks}\n"
                
                break

    with open("Report_card.txt","w") as rc:
        rc.writelines(all_lines)
    print("Marks added successfully")

def Calculate():
    who = input("Name of the student: ")
    with open("Report_card.txt","r") as rc:
        all_lines = rc.readlines()
        for i in range(len(all_lines)):
            check = all_lines[i].strip().split(",")
            if check[0] == who:
                print("Student Found!!")
                calc = ((int(check[2]) + int(check[3]) + int(check[4]) + int(check[5]) + int(check[6]))/500)*100
                all_lines[i] = f"{check[0]},{check[1]},{check[2]},{check[3]},{check[4]},{check[5]},{check[6]},{calc}%\n"
                break
        else:
            print("Student Not Found!!")
            return
    with open("Report_card.txt","w") as rc:
        rc.writelines(all_lines)
    print(f"Percentage calculated of {who} and percentage is {calc}")
        
def View():
    with open("Report_card.txt","r") as rc:
        print(rc.read())
    
def Search():
    who = input("Enter the name of the student: ")
    with open("Report_card.txt","r") as rc:
        all_lines = rc.readlines()
        for i in all_lines:
            check = i.strip().split(",")
            if check[0] == who:
                check = ",".join(check)
                break

            else:
                print("No student found!")
    print(check)

def delete():
    who = input("Enter the name of the student: ")
    with open("Report_card.txt","r") as rc:
        all_lines = rc.readlines()
        for i in all_lines:
            check = i.strip().split(",")
            if check[0] == who:
                print("Student Found!")
                all_lines.remove(i)
                break
        else:
            print("Something went wrong")
            return
    with open("Report_card.txt","w") as rc:
        rc.writelines(all_lines)

def Exit():
    print("Exiting the menu.....")
    return

def menu():
    while(True):
        print("!WELCOME TEACHER!")
        print("What you want to do\n1)Add student\n2)Add student marks\n3)Calculate\n4)View all students\n5)Search student\n6)delete any student\n7)Exit..")
        choose = input("Enter your choice:")
        if choose == '1' and choose.isdigit():
            Add()
        if choose == '2' and choose.isdigit():
            Add_student_marks()
        if choose == '3' and choose.isdigit():
            Calculate()
        if choose == '4' and choose.isdigit():
            View()
        if choose == '5' and choose.isdigit():
            Search()
        if choose == '6' and choose.isdigit():
            delete()    
        if choose == '7' and choose.isdigit():
            Exit()
            return
    
menu()