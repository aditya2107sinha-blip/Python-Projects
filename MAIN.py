# TO DO LIST PROJECT #

ToDo_List = []

def Add():
    task = input("Enter the task you want: ")
    ToDo_List.append({"task":task, "Status":"pending"})
    print("New task Added succesfully\n")

def Remove():
    
    if len(ToDo_List)==0:
        print("No task to remove")
    else:
        try:
            search_index = int(input("enter the index you want to remove: "))-1
            if 0 <= search_index < len(ToDo_List):
                ToDo_List.pop(search_index)
                print("Task has been removed successfully!!")

            else:
                print("something went wrong")
        except ValueError:
            print("please enter a valid number")
            print("\n")



def View():
    if len(ToDo_List)==0:
        print("No task pending!!!!")

    else:
        for index,task in enumerate(ToDo_List,1):
            print(f"{index}: {task['task']}- {task['Status']}\n")  # yaha pe jo ye task h woh pura dictionary h jo list mein gaya h toh usme se bhai 'task' key ki value maang rahe h same status bhi maaang raha h 


def Complition():
    if len(ToDo_List)==0:
        print("No task to remove")
    else:
        search_index = int(input("enter the index you want to mark as done : "))-1
        if 0 <= search_index < len(ToDo_List):
            change = ToDo_List[search_index]
            change['Status'] = "Done"
            for index,change in enumerate(ToDo_List,1):
                print(f"{index}: {change}" )
                


def Invalid():
    print("You are doing something wrong\nPlease check")


def menu():
    while(True):
        print("*** MAIN MENU ***")
        print("1. Add a task")
        print("2. View all task")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")
        Choice = int(input("Enter your choice:"))

        if Choice == 1:
            Add()
        elif Choice == 2:
            View()
        elif Choice == 3:
            Remove()
        elif Choice == 4:
            Complition()
        elif Choice == 5:
            print("Exiting the programm....")
            break
        else:
            Invalid()


menu() 
