# prompt user to enter a pragraph.
# split the text using the fullstop
# capitalize using the index or any letter after a fullstop


paragraph = input("Enter text: ")
split_paragraph = paragraph.split(".")
result = []
for word in split_paragraph:
    word = word.strip()

    if word != "":
        capitalized = word[0].upper() + word[1:]
        result.append(capitalized)

final_text = ". ".join(result)
print("Capitalized:", final_text)
