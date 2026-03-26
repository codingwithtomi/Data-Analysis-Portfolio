# Write a list of names and assign a variable.
# Print the list
# Prompt user to enter a name to remove(pop)
# If name is in list, print yada yada yada
# Remove the name and print the updated list
# And if user enters a name that is not in the list, print an error message

current_list = ["Alice", "Bob", "Charlie", "Diana"]
print(current_list)

name = input("Enter name to remove: ")
if name in current_list:
    current_list.remove(name)
    print(f"Updated list: {current_list}")
else:
    print(f"'{name}' is not in the list")
