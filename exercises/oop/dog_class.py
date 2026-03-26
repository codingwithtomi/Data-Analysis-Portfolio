class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

    def describe(self):
        print(f"{self.name} is a {self.breed}")


my_dog = Dog("Tough", "Rottweiler")
the_dog = Dog("Luna", "Chihuahua")
my_dog.bark()
my_dog.describe()
the_dog.bark()
the_dog.describe()
