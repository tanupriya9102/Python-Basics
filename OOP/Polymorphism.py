#In Object-Oriented Programming, any object or method has more than one name associated with it. That is nothing but polymorphism.

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Creating instances
dog = Dog()
cat = Cat()
cow = Cow()

# Using polymorphism in a function
def animal_sounds(animal):
    return animal.make_sound()

# Calling the function with different animals
print(animal_sounds(dog))
print(animal_sounds(cat))
print(animal_sounds(cow))
