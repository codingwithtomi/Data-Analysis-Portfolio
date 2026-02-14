year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# Python can perform mathematical calculations using operators:
# + addition
# - subtraction
# * multiplication
# / division (always gives a decimal result)
# // integer division (rounds down to whole number)
# % modulo (gives the remainder after division)
# ** exponentiation (powers)
# To do math with user input, you must convert the text to a number using int() for whole numbers or float() for
# decimals.
