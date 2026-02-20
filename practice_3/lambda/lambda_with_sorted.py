#example 1 with sorted() and lambda
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#example 2 with sorted() and lambda
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#example 3 with sorted() and lambda
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)

#example 4 with sorted() and lambda
people = [{"name": "Emil", "age": 25}, {"name": "Tobias", "age": 22}, {"name": "Linus", "age": 28}]
sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)

#example 5 with sorted() and lambda
data = [("Emil", 25, "A"), ("Tobias", 22, "B"), ("Linus", 28, "A"), ("Anna", 24, "C")]
sorted_data = sorted(data, key=lambda x: (x[2], x[1]))
print(sorted_data)