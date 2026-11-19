class Animal:

    def __init__(self, name: str):
        self.name = name


# Dog inherits from Animal
class Dog(Animal):

    def bark(self):
        return f"{self.name} says Woof!"


# Usage
my_dog = Dog("Buddy")
print(my_dog.bark())