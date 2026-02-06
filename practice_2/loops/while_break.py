#example 1
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# This will print 1, 2, 3 and then exit the loop when i equals 3

#example 2
i = 1
while i < 6:
    if i == 4:
        break
    print(i)
    i += 1  
# This will print 1, 2, 3 and then exi

#example 3
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)  # Only odd numbers: 1, 3, 5, 7, 9

#example 4
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
skip_list = ['banana', 'date']

for fruit in fruits:
    if fruit in skip_list:
        continue  # Skip banana and date
    print(f"Processing {fruit}")
# Output: Processing apple, Processing cherry, Processing elderberry

#example 5
# Skip numbers divisible by 3
count = 0
while count < 10:
    count += 1
    if count % 3 == 0:
        continue  # Skip numbers divisible by 3
    print(count)  # 1, 2, 4, 5, 7, 8, 10t the loop when i equals 4


