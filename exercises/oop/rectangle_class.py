class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(4, 4)
rectangle3 = Rectangle(10, 2)

print("Rectangle1:", rectangle1.width, "x", rectangle1.height)
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())
print("Is square:", rectangle1.is_square())

print("Rectangle2:", rectangle2.width, "x", rectangle2.height)
print("Area:", rectangle2.area())
print("Perimeter:", rectangle2.perimeter())
print("Is square:", rectangle2.is_square())

print("Rectangle3:", rectangle3.width, "x", rectangle3.height)
print("Area:", rectangle3.area())
print("Perimeter:", rectangle3.perimeter())
print("Is square:", rectangle3.is_square())
