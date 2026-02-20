#example 1 lambda with filter()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered_list)

#example 2 filter() with function
def is_even(n):
    return n % 2 == 0
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(is_even, my_list))
print(filtered_list)

#example 3 filter() with lambda and list comprehension
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = [x for x in my_list if (lambda x: x % 2 == 0)(x)]
print(filtered_list)

#example 4 filter() with lambda and map()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x % 2 == 0, map(lambda x: x, my_list)))
print(filtered_list)

#example 5 filter() with lambda 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x > 5, my_list))
print(filtered_list)
