#example 1
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#example 2
def my_function(**kwargs):
  for key, value in kwargs.items():
    print(key + ": " + value)

my_function(name = "Alice", age = "30", city = "New York")

#example 3 Sending a list as an argument
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#example 4 Sending a dictionary as an argument
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

#example 5 with return 
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

