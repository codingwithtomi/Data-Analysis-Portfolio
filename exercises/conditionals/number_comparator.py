number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print(f"{number1} is larger than {number2}.")
elif number2 > number1:
    print(f"{number2} is larger than {number1}.")
else:
    print("Both numbers are equal.")
