# Prompt user to type a number from 1-7
# Each number represents the days of the week with Monday being the first day
# Create a list of the weekdays
# assign the numbers to each weekday in the form of an index


weekdays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
number = int(input("Enter day number(1-7): "))

if 1 <= number <= 7:
    index = number - 1
    print(weekdays[index])
else:
    print("Invalid input")
