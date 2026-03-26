inventory = {"apples": 8, "oranges": 3, "bananas": 10}
while True:
    choice = input("Choose an option:\n "
                   "1- Add/Update item\n"
                   "2- Check item\n"
                   "3- Quit.\n")
    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        if item in inventory:
            inventory[item] += quantity
            print(f"{item}: {inventory[item]} in stock.")
        else:
            inventory[item] = quantity
            print(f"{item} added to inventory. Quantity: {inventory[item]}")
    elif choice == "2":
        check = input("Enter item to check: ")
        if check in inventory:
            print(f"{check}: {inventory[check]} in stock.")
        else:
            print(f"{check} not in inventory.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
