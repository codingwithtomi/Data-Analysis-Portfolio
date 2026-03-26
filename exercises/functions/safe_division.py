try:
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    result = first / second
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
