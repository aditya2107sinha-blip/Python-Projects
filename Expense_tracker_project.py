#### EXPENSE TRACKER ####

class expense_tracker():
    category = []
    expense = []
    def Add(self):
        while (True):
            Add_category = input("What kind expense is this? ")
            Add_expense = int(input("Enter the amount you spend:"))
            self.category.append(Add_category)
            self.expense.append(Add_expense)
            end = input("Do you want to Exit Adding section?(y/n) ")
            with open("Expense_diary.txt","a") as ed:
                ed.write(f"{Add_expense},{Add_category}\n")
            if end == "y":
                print("Exiting the Adding section...")
                break


    def View(self):
        with open("Expense_diary.txt","r") as ed:
            print(ed.read())
    def Total(self):
        with open("Expense_diary.txt","r") as ed: 
            total = 0  
            all_lines = ed.readlines()
            for i in all_lines:
                data = i.strip().split(",")
                total += int(data[0]) 

            print(f"Your total weekly spending is {total}")
                
    def Highest(self):
        maximum = float("-inf")
        with open("Expense_diary.txt","r") as ed: 
            arr = []  
            all_lines = ed.readlines()
            for i in all_lines:
                data = i.strip().split(",")
                arr.append(data[0])
            for _ in arr:
                if float(_) > float(maximum):
                    maximum = float(_)
        print(f"The highest you spend amount is {maximum}") 

    def Weekly_Avg(self):
        with open("Expense_diary.txt","r") as ed: 
            total = []  
            all_lines = ed.readlines()
            for i in all_lines:
                data = i.strip().split(",")
                total.append(int(data[0])) 
            total_week_spending = 0
            for i in total:
                total_week_spending += i

            weekly_avg = (total_week_spending)/len(total)
        print(f"Your Average Weekly spending is {weekly_avg}")

    def Search(self):
        whos = input("Who's spending you want to search? ")
        with open("Expense_diary.txt","r") as ed:
            all_lines = ed.readlines()
            for _ in all_lines:
                data = _.strip().split(",")
                if data[1] == whos.lower():
                    print("Spending found!!!")
                    print(f"The spending on the {whos} category is {data[0]}")

                
        
        

    

class Menu(expense_tracker):
    def menu(self):
        while (True):
            print("WELCOME")
            choice = int(input("ENTER YOUR DECISION:\n1)Add Expenses\n2)View all Expenses\n3)Total Spending\n4)Highest Expense\n5)Weekly Expenses\n6)Search Expenses\n7)Exit..\n"))
            match choice:
                case 1:
                    self.Add()
                case 2:
                    self.View()
                case 3:
                    self.Total()
                case 4:
                    self.Highest()
                case 5:
                    self.Weekly_Avg()
                case 6:
                    self.Search()
                case 7:
                    print("Signing Off.....")
                    return



person_1 = Menu()
person_1.menu()