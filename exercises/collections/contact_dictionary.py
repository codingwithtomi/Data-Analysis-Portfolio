# Create a dictionary
# Prompt user to enter a name
# If name is in dictionary, print the corresponding phone number
# else, print an error message


data = {"Alice": "555-1234", "Bob": "555-5678", "Carol": "555-9999"}
name = input("Enter name: ")
data["Alice"] = "555-2222"
data["Alex"] = "555-2424"

if name in data:
    print(f"{name}'s number is {data[name]}.")
else:
    print("Contact not found")
