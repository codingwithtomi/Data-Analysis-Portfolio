# prompt user to enter a word
# if len is even, cut from the middle and separate
# if len is odd, add the middle to both halves
# print


word = input("Enter a word: ").strip()
half = len(word) // 2
if len(word) % 2 == 0:
    first_half = word[0:half]
    last_half = word[half:]
elif len(word) % 2 != 0:
    first_half = word[0:half+1]
    last_half = word[half:]

print(f"first_half: {first_half}")
print(f"last_half: {last_half}")


# if len(word) % 2 == 0:
