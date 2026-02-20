#example 1 add 10
x = lambda a : a + 10
print(x(5))

#example 2 multyply 
x = lambda a, b : a * b
print(x(5, 6))

#example sum of 3 numbers
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#example 4 lambda with filter()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x % 2 == 0, my_list)) 
print(filtered_list)

#example 5 
def myfunc(n):
  return lambda a : a * n
