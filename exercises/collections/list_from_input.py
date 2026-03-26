# number1 = int(input("Enter number 1: "))
# number2 = int(input("Enter number 2: "))
# number3 = int(input("Enter number 3: "))

numbers = []
for i in range(3):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)
print(f"Your numbers: {numbers}")
