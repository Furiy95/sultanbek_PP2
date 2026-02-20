#example 1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#example 2 create child
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()

#example 3
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.


#example 4 add __init__() function to the child class
class Student(Person):  
    def __init__(self, fname, lname, year):  
        Person.__init__(self, fname, lname)  
        self.graduationyear = year
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear) 

