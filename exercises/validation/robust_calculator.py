# create an infinite loop that breaks when you type quit.
# prompt user to type a calculation
# if input == "quit", print goodbye and break
# split input using space
# if it is not in 3 parts, print error message
# if it is in 3 parts, convert first and third part to number
# store operator in a variable.
# if operator is "+", result = a + b. print result
# if operator is "-", result = a - b. print
# if operator is "*", result = a * b, print
# if operator is "/", result = a / b, print
# else display error message unknown operator
# except an error division, print error message
# except value error, print error message

print("Calculator (type 'quit' to exit)")
while True:
    calculator = input("> ")
    if calculator == "quit":
        print("Goodbye!")
        break
    try:
        split_calculator = calculator.split()
        if len(split_calculator) != 3:
            print("Error: Invalid format")
            continue
        else:
            first = float(split_calculator[0])
            operator = (split_calculator[1])
            second = float(split_calculator[2])
            if operator == "+":
                result = first + second
                print(result)
            elif operator == "-":
                result = first - second
                print(result)
            elif operator == "*":
                result = first * second
                print(result)
            elif operator == "/":
                result = first / second
                print(result)
            else:
                print(f"Error: unknown operator {operator}. Use +,-,*,/")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Invalid format. Use: number operator number")
