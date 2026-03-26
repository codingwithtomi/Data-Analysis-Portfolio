# create an empty dictionary{}
# use an infinite loop
# prompt user to add command to the dictionary and store it in a variable
# split the item in the variable
# set the action as the first word, item as the second word and quantity as the third word
# convert quantity to an integer
# if the action = add and a particular item has not been added before, add the item to inventory and add the quantity
# then print "added quantity item"
# if the item exists, add the quantity to the one that already exists
# print "updated item to new quantity"
# if user inputs check + item, print "item: quantity in stock"
# if item does not exist, print "item not in inventory"
# if first word is list, print inventory and list all the items in it. (item: quantity)
# if action is quit, break and print Goodbye!


inventory = {}

while True:
    command = input("Command: ").strip().lower()
    parts = command.split()

    action = parts[0]

    if action == "add" and len(parts) == 3:
        item = parts[1]
        quantity = int(parts[2])

        if item in inventory:
            inventory[item] += quantity
            print(f"Updated {item} to {inventory[item]}.")
        else:
            inventory[item] = quantity
            print(f"Added {quantity} {item}.")

    elif action == "check" and len(parts) == 2:
        item = parts[1]
        if item in inventory:
            print(f"{item}: {inventory[item]} in stock")
        else:
            print(f"{item} not in inventory.")

    elif action == "list":
        if inventory:
            print("Inventory:")
            for item, quantity in inventory.items():
                print(f"- {item}: {quantity}")
        else:
            print("Inventory is empty.")

    elif action == "quit":
        print("Goodbye!")
        break

    else:
        print("Invalid command. Try add/check/list/quit.")
