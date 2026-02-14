number = int(input("Enter a number: "))

if number < 0:
    print(f"{number} is negative")
elif number > 0:
    print(f"{number} is positive")
else:
    print("Zero is neither positive nor negative")
