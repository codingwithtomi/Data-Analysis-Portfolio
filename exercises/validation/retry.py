# create an empty dictionary
# print (word counts:)
# prompt user to input a sentence
# split said sentence using spaces sentence.split()
# loop over the sentence
# if a word has appeared before, count it as one
# else, add 1 everytime said word is repeated
#
import string

word = {}
print("Word counts:")
sentences = input("Enter a sentence: ").lower()
split_sentence = sentences.split()

for x in split_sentence:
    x = x.strip(string.punctuation)

    if x in word:
        word[x] += 1
    else:
        word[x] = 1

for x, counts in word.items():
    print(f"{x}: {counts}")
