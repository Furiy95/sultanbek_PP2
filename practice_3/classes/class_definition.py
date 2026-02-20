#example 1 create class
class MyClass:
  x = 5

#example 2 create object
p1 = MyClass()
print(p1.x)


#example 3 class Person:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Emil", 25)
print(p1.name)
print(p1.age)

#example 4 class with method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil", 25)
p1.myfunc()


