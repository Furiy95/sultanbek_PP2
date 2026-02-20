#example 1 lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#example 2 filter() with lambda and map()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x % 2 == 0, map(lambda x: x, my_list)))
print(filtered_list)

#example 3 filter() with lambda and map()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x > 5, map(lambda x: x, my_list)))
print(filtered_list)

#example 4 filter() with lambda and map()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, my_list)))
print(filtered_list)

#example 5 filter() with lambda and map()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x > 5, map(lambda x: x * 2, my_list)))
print(filtered_list)
