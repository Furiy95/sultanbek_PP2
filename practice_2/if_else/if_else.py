#example 1 of if-elif-else statement in python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#example 2
score = 75

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#example 3 chech even or odd
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")


#example 4 temperature check
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#example 5 valid user input
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
  
