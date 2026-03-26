# foods = ["pizza", "sushi", "tacos", "pasta", "burgers"]
# print("My favorite foods:")

# for count, food in enumerate(foods, start=1):
#     print(f"{count}. {food}")

foods = ["pizza", "sushi", "tacos", "pasta", "burgers"]
count = 0
print("My favorite foods: ")
for food in foods:
    count += 1
    print(count, food)
