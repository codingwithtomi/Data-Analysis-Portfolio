# def say_hi():
#     print("Hi!")


# for x in range(3):
#     say_hi()


\
# def say_hi(name):
#     print(f"Hi, {name}!")


# say_hi("Aliice")
# say_hi("Bob")
# say_hi("Tomisin")


\
# numbers = [2, 5, 7, 10]


# def double_number(num):
#     return num * 2


# for num in numbers:
#     print(double_number(num))


def double_number(num):
    return num * 2


def double_list(nums):
    numbers = []
    for x in nums:
        doubled_value = double_number(x)
        numbers.append(doubled_value)
    return numbers


number = [2, 5, 7, 10]
print(double_list(number))
