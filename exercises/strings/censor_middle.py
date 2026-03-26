# prompt user to enter a word
# assign variable to first, middle and last letters
# replace middle with asteriks
# join and print


word = input("Enter word: ").strip()

first_letter = word[:1]
last_letter = word[-1:]
middle = word[1:-1]
asteriks = "*" * len(middle)
final = "".join([first_letter, asteriks, last_letter])
print("Censored: ", final)
