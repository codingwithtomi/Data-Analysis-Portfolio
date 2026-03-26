while True:
    number = int(input("Enter a number(1-10): "))
    if 1 <= number <= 10:
        print(f"Thank you! You entered {number}.")
        break
    else:
        print("Invalid! Try again.")
