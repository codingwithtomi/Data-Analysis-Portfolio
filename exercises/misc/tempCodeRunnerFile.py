inventory = {"apples": 5, "oranges": 3, "bananas": 8}
inventory["apples"] = inventory["apples"] + 3
inventory["bananas"] += 2
print(inventory)

n = int(input("How many times do you want to add/update?: "))
for i in range(1, n+1):
    item = input("Enter item: ")
    quantity = int(input("Enter quantity: "))
    if item in inventory:
        inventory[item] += quantity
        print(f"{item}: {inventory[item]} in stock")
    else:
        inventory[item] = quantity
        print(f"{item}: {inventory[item]} added to inventory")

check = int(input("How many times do you want to check?: "))
for x in range(1, check+1):
    check_item = input("Enter item to check: ")
    if check_item in inventory:
        print(f"{check_item}: {inventory[check_item]} in stock.")
    else:
        print(f"{check_item} not in inventory")
