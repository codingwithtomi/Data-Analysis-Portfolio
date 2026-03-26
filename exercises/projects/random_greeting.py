# import random
# create a list called greeting that contains random greetings
# define say_hello
# print random greeting from list (for loop?)
# use random.choice somewhere
# for loop(range) call it 5 times

import random


def say_hello():
    greeting = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Howdy!"]
    x = random.choice(greeting)
    print(x)


for i in range(5):
    say_hello()
