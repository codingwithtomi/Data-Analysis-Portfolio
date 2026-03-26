# Prompt user to type number 5 times (loop?)
# Store them in a list (append?)
# Print list, sort in asc and desc order

numbers = []
for i in range(5):
    number = int(input(f"Number {i + 1}: "))
    numbers.append(number)
print(f"Original: {numbers}")
numbers.sort()
print(f"Sorted (ascending): {numbers}")
numbers.sort(reverse=True)
print(f"Sorted(descending): {numbers}")
