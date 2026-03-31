def contact_book():
    while True:
        print('''1) Add contact\n2) View all contact\n3) Search contact\n4) Delete contact\n5) Exit''')
        Your_choice = int(input("Enter your choice: "))
        if Your_choice == 1:
            What = input("What name do you want to add: ").strip()
            What_2 = int(input("there contact number: "))
            with open("Contact_Book.txt","a") as cb:
                cb.write(f"{What},{What_2}\n")
        elif Your_choice == 2:
            with open("Contact_Book.txt","r") as cb:
                content = cb.read()
                print(content)

        elif Your_choice == 3:
            Search = input("Whom you want to search:").strip()
            with open("Contact_Book.txt","r") as cb:
                for lines in cb:
                    if Search in lines:
                        print(lines)
                        break
                else:
                    print("No such contact found")
        elif Your_choice == 4:
            Search_2 = input("Whose contact you want to delete:").strip()
            with open("Contact_Book.txt","r") as cb:
                all_lines = cb.readlines()
                new_lines = []
                for linea in all_lines:
                    if Search_2.lower() not in linea.lower():
                        new_lines.append(linea)
                with open("Contact_Book.txt","w") as cb:
                    cb.writelines(new_lines)
        elif Your_choice == 5:
            print("Exiting the code.......")
            break






                        
                        
            

                




contact_book()