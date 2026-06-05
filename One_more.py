import sys
class Customer_Menu():
    def __init__(self):
        self.names = []
    def Show_all_product(self):
        with open("Stock.txt","r") as st:
            print(st.read())
    def Add_to_Cart(self):
        while(True):
            i = input("Enter your name: ")
            self.names.append(i)
            with open(f"{i}.txt","w") as it:
                with open("Orders.txt","a") as ot:
                    while(True):
                        what = input("Enter the item you want to add: ")
                        how_much = input("Enter the quantity: ")
                        date = input("Any particular date of recieving this order? ")
                        it.write(f"{i},{what},{how_much},{date}\n")
                        ot.write(f"{i},{what},{how_much},{date}\n")

                        choose = input("Do you want to add more?(y/n) ")
                        if choose.lower() == 'n':
                            return
    def Search(self):
        what = input("Enterthe name of product you want: ")
        with open("Stock.txt","r") as st:
            all_lines = st.readlines()
            for i in all_lines:
                data = i.strip().split()
                if data[0] == str(what):
                    print(f"{"".join(i)}")
                    print("This item is available")
                    break
            else:
                print("Item Not Found!!")
    def CheckOut(self):
        print("Thanks for Shopping from us..")
        return
    def Order_history(self):
        Name = input("Please enter your name: ")
        try:
            with open(f"{Name}.txt","r") as Nt:
                print(Nt.read())
        except FileNotFoundError:
            print("You have no order history")
    def Exit(self):
        print("Heading you out")
        sys.exit()
                


        

class Owner_Menu(Customer_Menu):
    def Add(self):
        while(True):
            Item_to_add = input("Enter the name of the item: ")
            quantity = input("Enter the qantity of this Product: ")
            Per_piece_price = input("Enter the price for per piece: ") 
            with open("Stock.txt","a") as st:
                st.write(f"{Item_to_add},{quantity},{Per_piece_price}\n")
            choose = input("More To add? ")
            if choose == "n":
                break
    def View(self):
        with open("Stock.txt","r") as st:
            print(st.read())

    def Checking_orders(self):
        for index , name in enumerate(self.names):
            print(f"{index}) {name}")
        print("This are names who have placed order")
        who = input("Name of the person who's order to check first: ")
        try:
            with open(f"{who}.txt","r+") as wtf:
                print(wtf.read())
                tell = input("Do we have this Products?(y/n) ")
                if tell == "y":
                    wtf.seek(0,2)
                    wtf.write("We have this Products\nThe product will get delivered to you at time..")
                    print("Order status updated successfully")
                elif tell == "n":
                    wtf.seek(0,2)
                    wtf.write("We don't have this product\nSorry for inconvinience...")
                    print("Order status updated successfully")
        except FileNotFoundError:
            print(f"Error: No order file found for '{who}'")
            
    def Exit(self):
        print("Heading you out")
        sys.exit()

            


Tell_me = input("Are you Owner or Customer? (o/c)")
if Tell_me == "o":
    owner_obj = Owner_Menu()
    while(True):
        what_we_can_do = int(input("What you want to do\n1)Add products\n2)View\n3)Check order\n4)exit\n"))
        match what_we_can_do:
            case 1:
                owner_obj.Add()
            case 2:
                owner_obj.View()
            case 3:
                owner_obj.Checking_orders()
            case 4:
                owner_obj.Exit()

elif Tell_me.lower().strip() == "c":
    customer_obj = Customer_Menu()
    while(True):
        what_to_do = int(input("What you want to do\n1) View all products\n2) Search\n3) Add to cart\n4) Checkout\n5) Order history\n6) Exit\n"))
        match what_to_do:
            case 1:
                customer_obj.Show_all_product()
            case 2:
                customer_obj.Search()
            case 3:
                customer_obj.Add_to_Cart()
            case 4:
                customer_obj.CheckOut()
            case 5:
                customer_obj.Order_history()
            case 6:
                customer_obj.Exit()