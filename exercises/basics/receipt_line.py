item = input("Item name: ")
quantity = int(input("Quantity: "))
price = float(input("Price per item: "))
total_cost = quantity * price

print(f"{item}*({quantity}).........${total_cost:.2f}")
