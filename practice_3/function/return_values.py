#example 1
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#example 2
def my_function():
  return "Hello, World!"
greeting = my_function()
print(greeting)

#example 3 function return tuple
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

#examlpe 4 You can specify that a function can have ONLY positional arguments
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

#example 5 wrong test
def my_function(name, /):
  print("Hello", name)

my_function(name = "Emil")
