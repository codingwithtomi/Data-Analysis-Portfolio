# write a function called factorial which takes one parameter
# create a for loop that loops through range(1, parameter + 1)
# multiply everything and store in variable called result
# return result and print


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


print(factorial(5))
print(factorial(0))
print(factorial(7))
