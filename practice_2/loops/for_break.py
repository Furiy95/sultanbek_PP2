#example 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#example 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#example 3
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#example 4
for x in range(2, 6):
  if x == 4: break
  print(x)

#example 5
for x in "banana":
  if x == "n": break
  print(x)
  