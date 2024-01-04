#single inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create an instance of Dog
my_dog = Dog()

# Access methods from both Animal and Dog classes
my_dog.speak()  # Output: Animal speaks
my_dog.bark()   # Output: Dog barks

#multiple inheritance
class Flyable:
    def fly(self):
        print("Can fly")

class Swimable:
    def swim(self):
        print("Can swim")

class Duck(Flyable, Swimable):
    def quack(self):
        print("Duck quacks")

# Create an instance of Duck
my_duck = Duck()

# Access methods from Flyable, Swimable, and Duck classes
my_duck.fly()    # Output: Can fly
my_duck.swim()   # Output: Can swim
my_duck.quack()  # Output: Duck quacks

#multilevel inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Labrador(Dog):
    def fetch(self):
        print("Labrador fetches")

# Create an instance of Labrador
my_labrador = Labrador()

# Access methods from Animal, Dog, and Labrador classes
my_labrador.speak()  # Output: Animal speaks
my_labrador.bark()   # Output: Dog barks
my_labrador.fetch()  # Output: Labrador fetches
