data = {"Alice": "555-1234", "Bob": "555-5678", "Carol": "555-9999"}

name = input("Enter name: ")
if name in data:
    print(f"{name}'s number is {data[name]}")
else:
    print("Contact not found.")
