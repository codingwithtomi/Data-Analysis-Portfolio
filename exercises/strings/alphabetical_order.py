word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if word1 < word2:
    print(f"{word1} comes before {word2} alphabetically.")
elif word2 < word1:
    print(f"{word2} comes before {word1} alphabetically.")


# Use < when you want to say something comes before something
# Use > when you want to say something comes after something
