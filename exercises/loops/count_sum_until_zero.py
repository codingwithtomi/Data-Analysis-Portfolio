count = 0
total = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    count += 1
    total += number

print("Count:", count)
print("Total:", total)

if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No numbers added")
