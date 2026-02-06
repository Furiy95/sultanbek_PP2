#example 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#example 2
for x in range(6):
  if x == 3:
    continue
  print(x)
else:
  print("Finally finished!")    

#example 3
for x in range(2, 6):
  if x == 4:
    continue
  print(x)  

#example 4
for x in "banana":
  if x == "n":
    continue
  print(x)  

#example 5
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
  if num % 2 == 0:
    continue
  print(num)
# This will print only odd numbers: 1, 3, 5