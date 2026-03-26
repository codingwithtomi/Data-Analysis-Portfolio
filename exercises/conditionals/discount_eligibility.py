member = input("Are you a member? (yes/no): ")
amount = float(input("Purchase amount: "))

if member == "yes" or amount >= 100:
    print("You qualify for a discount!")
else:
    print("No discount available.")
