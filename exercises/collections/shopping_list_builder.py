# Create an empty list and assign a variable
# Prompt user to enter x number of items till they type done (loop, range?, append)
# Create an infinite loop, if word == done, break then print the stuff
# When they type done, loop breaks
# Print final list and count


item = []

while True:
    word = input("Enter item('or done'): ")

    if word == "done":
        break
    item.append(word)

print("Shopping List:")
for x in item:
    print(f"- {x}")

print(f"Total: {len(item)} items")
