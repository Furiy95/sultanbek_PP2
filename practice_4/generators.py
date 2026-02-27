#example 1
def squares_up_to_n(N):
    for i in range(N + 1):
        yield i * i

N = int(input())
for square in squares_up_to_n(N):
    print(square, end=" ")


#example 2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

even_nums = list(even_numbers(n))
print("Even numbers:", ", ".join(map(str, even_nums)))

#example 3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i

n = int(input())
print(f"Numbers divisible by both 3 and 4 between 0 and {n}:")
for num in divisible_by_3_and_4(n):
    print(num, end=" ")

#example 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Test with a for loop
a = int(input("start: "))
b = int(input("end: "))

print(f"Squares of numbers from {a} to {b}:")
for value in squares(a, b):
    print(f"{value}", end=" ")

#example 5
def countdown(n):
    for i in range(n, -1, -1):
        yield i
    
n = int(input(""))
print(f"Numbers from {n} down to 0:")
for num in countdown(n):
    print(num, end=" ")