#example 1
class Animal:
    def speak(self):
        print("The animal makes a generic sound.")

class Dog(Animal):
    def speak(self):
        print("Bark! Bark!")

# Usage
generic_animal = Animal()
specific_dog = Dog()

generic_animal.speak()  # Output: The animal makes a generic sound.
specific_dog.speak()    # Output: Bark! Bark!

#example 2python
class Person:
    def introduce(self):
        print("Hello, I'm a person.")

class Programmer(Person):
    def introduce(self):
        super().introduce()  # Call the parent's introduce method
        print("And I write Python code.")

person = Person()
programmer = Programmer()

#example 3
class Parent(): 
	def show(self): 
		print("Inside Parent") 
		
class Child(Parent): 
	def show(self): 
		# Calling the parent's class 
		# method 
		super().show() 
		print("Inside Child") 
		
# Driver's code 
obj = Child() 
obj.show()

#example 4
class Vehicle:
    def start_engine(self):
        print("The engine starts with a generic sound.")
class Car(Vehicle):
    def start_engine(self):
        print("The car engine starts with a roar.") 
generic_vehicle = Vehicle()