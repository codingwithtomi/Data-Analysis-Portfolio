grade = int(input("Enter your score: "))

if 90 <= grade <= 100:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 70 <= grade <= 79:
    print("C")
elif 60 <= grade <= 69:
    print("D")
elif 0 <= grade <= 60:
    print("F")
else:
    print("Invalid score")
