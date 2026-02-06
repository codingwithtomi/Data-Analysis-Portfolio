# Send a prompt to the user
# Split user_input into words
# check if echo is the first word
# if echo is the first word, print the remaining words after echo
# elif words[0] == exit, break
# else, print an error message
# Go back to step 1

while True:
    user_input = input("PS C:\\Users\\USER> ")

    words = user_input.split()
    first_word = words[0]
    if first_word == "echo":
        for i in range(1, len(words)):
            print(words[i])
    elif first_word == "exit":
        break
    else:
        print("Error : Command not recognized")
