# We want a menu that keeps appearing until the user chooses 3.
choice = 0

while choice != 3:
    # show menu
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    # take choice
    choice = int(input("Enter your choice: "))
    # handle choice
    if choice == 1:
        print("Hello!")
    elif choice == 2:
        print("Goodbye!")
    elif choice == 3:
        print("Exiting...")
        break # break not necessary here as if choice == 3, the while loop will exit anyway
    else:
        print("Invalid choice. Please try again.")
    

