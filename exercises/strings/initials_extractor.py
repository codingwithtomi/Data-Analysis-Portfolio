# prompt user to enter full name
# split the full name into separate words
# extract the first letter of all words
# convert all extracted letters to uppercase
# join them
# print


name = input("Enter full name: ").strip()
split_name = name.split()
names = []
for word in split_name:
    capitalized = word[0].upper()
    names.append(capitalized)

final_text = "".join(names)
print(f"Initials: {final_text}")
