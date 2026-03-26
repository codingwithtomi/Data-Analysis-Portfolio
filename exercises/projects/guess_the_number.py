count = 0
secret_number = 7
while True:
    number = int(input("Guess the number: "))
    count += 1
    if number < secret_number:
        print("Too low!")
    if number > secret_number:
        print("Too high!")
    if number == secret_number:
        print(
            f"Correct! You got it in {count} guess{"es" if count > 1 else ""}.")
        break
