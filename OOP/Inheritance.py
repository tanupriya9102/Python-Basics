class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating instances
dog = Dog("Buddy", "Canine")
cat = Cat("Whiskers", "Feline")

# Accessing attributes and methods
print(f"{dog.name} is a {dog.species} and sounds like: {dog.make_sound()}")
print(f"{cat.name} is a {cat.species} and sounds like: {cat.make_sound()}")
