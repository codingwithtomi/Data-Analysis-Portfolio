# prompt user to write a sentence
# create empty dictionary, words
# convert sentence to lower case
# split sentence using a space and assign to variable split_sentence
# use a for loop to access the array
# if word in words, increase count
# else set value of the word to 1
# print word counts
# for word in words print word[words]


sentence = input("Enter a sentence: ")
words = {}
sentences = sentence.lower()
split_sentence = sentences.split(" ")

for word in split_sentence:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
print("Word counts:")

for word, count in words.items():
    print(f"{word}: {count}")
