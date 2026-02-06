#example 1
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
else:
  print("Finally finished!")    

#example 2
i = 1
while i < 6:       
    if i == 4:
        i += 1
        continue
    print(i)  
    i += 1


#example 3
i = 1
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
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
while i <= 10:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1 
# This will print numbers from 1 to 10 except multiples of 3