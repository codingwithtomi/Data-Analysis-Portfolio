# prompt user to enter a word
# split
# check if len == 1
# if yes, reverse. if no, print error message


word = input("Enter a word: ").strip()
words = word.split()

if len(words) == 1:
    reversed_word = word[::-1]
    print(f"Reversed: {reversed_word}")
else:
    print("Please enter one word!")
