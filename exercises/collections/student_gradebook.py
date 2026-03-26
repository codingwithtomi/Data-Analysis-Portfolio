data = {"Alice": 85, "Bob": 92, "Carol": 78, "David": 95, "Eve": 88}
print("Grade Book:")

for key, value in data.items():
    print(f"{key}: {value}")
average = sum(data.values()) / len(data)
print(f"Class average: {average}")
print(data.values())
