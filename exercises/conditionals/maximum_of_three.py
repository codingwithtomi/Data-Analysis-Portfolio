def max_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


print(max_of_three(5, 12, 8))
print(max_of_three(100, 50, 75))
print(max_of_three(3, 3, 3))
