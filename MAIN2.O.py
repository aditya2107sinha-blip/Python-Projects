#==== TO-DO LIST PHIRSE ====#
ToDo_list = []


def Add():
    task = input("enter the task you want to add:")
    ToDo_list.append({"Task":task , "Status":"Pending"})
    print("New task added successfully")


def View():
    if len(ToDo_list)==0:
        print("No task pending!!")
    else:
        for index,item in enumerate(ToDo_list,1):
            print(f"{index} : {item['Task']} - {item['Status']}")


def Remove():
    if len(ToDo_list) == 0:
        print("No task is added!!")
    else:
        try:
            search_index = int(input("enter the index of task you want to remove:")) - 1
            if 0 <= search_index < len(ToDo_list):
                ToDo_list.pop(search_index)
                print(ToDo_list)
                print("Task removed successfully...")

            else:
                print("something went wrong")

        except ValueError:
            print("Dekh ke ker bhai")


def Completion():
    if len(ToDo_list) == 0:
        print("No task is added!!")
    else:
        try:
            search_index = int(input("enter the index of task you want to remove:")) - 1
            if 0 <= search_index < len(ToDo_list):
                change = ToDo_list[search_index]
                change['Status'] = "Done"
                for index,changeing in enumerate(ToDo_list,1):
                    print(f"{index} : {changeing["Task"]} - {changeing["Status"]}")

            else:
                print("something went wrong")
        except ValueError:
            print("////Bhai thoda sa toh dekh ke\\\\") 


def Invalid():
    print("\\\\SOMETHING WENT WRONG////")
    

def menu():
    while(True):
        print("#### MAIN MENU ####")
        print("1. Add any task")
        print("2. view all task")
        print("3, Remove a task")
        print("4. mark as complete")
        print("5. Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            Add()
        elif choice == 2:
            View()
        elif choice == 3:
            Remove()
        elif choice == 4:
            Completion()
        elif choice == 5:
            print("Exiting the program.....")
            break
        else:
            Invalid()




menu()