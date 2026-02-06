#example 1
i = 1
while i < 6:
  print(i)
  i += 1

#example 2
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#example 3 
i = 1
while i < 6:         
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("i is no longer less than 6") 

#example 4
i = 0
while i < 6:
    i += 1
    if i % 2 == 0:
        continue
    print(i)    
# This will print only odd numbers: 1, 3, 5


#example 5
i = 1
while i <= 5:
    print(i)
    i += 1  
# This will print numbers from 1 to 5