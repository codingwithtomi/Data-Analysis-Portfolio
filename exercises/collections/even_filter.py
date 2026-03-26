limit = int(input("Enter limit: "))

even_numbers = [n for n in range(1, limit + 1) if n % 2 == 0]
print(f"Even numbers: {even_numbers}")
