# define a function that takes one parameter.
# return pi * r * r
# round result to 2 decimal places
# print


def circle_area(radius):
    return round(3.14159 * (radius ** 2), 2)


area1 = circle_area(5)
area2 = circle_area(2.5)
print(f"Area with radius 5: {area1} ")
print(f"Area with radius 2.5: {area2}")
