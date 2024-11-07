def phonebook_manager():
    phonebook = {}
    while True:
        print("Phonebook Manager")
        print("======================")
        print("Press '+' to add new contact")
        print("Press '-' to delete contact")
        print("Press 'f' to find a contact")
        print("Press 'p' to print all contacts")
        print("Press 'q' to quit the program")
        print("======================")
        print()
        choice = input("Your choice: ").strip() #remove whitespace

        if choice == '+':
            name = str(input("Enter name: "))
            
            try : 
                number = int(input("Enter phone number: "))
                
            except ValueError:
                print("number isnt integer. Try again")
                continue
            
            phonebook[name] = number
            print(f"Contact {name} added\n")

        elif choice == '-':
            name = input("Enter name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Contact {name} deleted.\n")
            else:
                print(f"Contact {name} not found.\n")

        elif choice == 'f':
            name = input("Enter name to find: ")
            if name in phonebook:
                print(f"{name}'s phone number is {phonebook[name]}.\n")
            else:
                print(f"Contact {name} not found.\n")

        elif choice == 'p':
            if phonebook:
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
                print("======================")
            else:
                print("Phonebook is empty.\n")

        elif choice == 'q':
            break
        else:
            print("Invalid choice.\n")

phonebook_manager()