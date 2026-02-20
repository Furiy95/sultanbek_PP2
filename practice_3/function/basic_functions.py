#example 1 basic functions
def my_function():
  print("Hello from a function")

#example 2 
def my_function():
  print("Hello from a function")
my_function()

#example 3
def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

#example 4 repetitive
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

#example 5 form fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))