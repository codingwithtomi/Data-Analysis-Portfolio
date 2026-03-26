data = ["apple", "banana", "cherry", "date", "elderberry"]

try:
    print(f"Items: {data}")
    index = int(input("Enter index (0-4): "))
    print(f"Item at index {index}: {data[index]}")
except ValueError:
    print("Error: Please enter a valid number.")
except IndexError:
    print("Error: Index out of range.")
