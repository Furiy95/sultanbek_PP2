# Example 1: AND operator
has_ticket = True
has_money = True
can_enter = has_ticket and has_money
print(f"Can enter: {can_enter}")  # True

# Example 2: OR operator
is_weekend = False
is_holiday = True
day_off = is_weekend or is_holiday
print(f"Day off: {day_off}")  # True

# Example 3: NOT operator
is_raining = True
is_dry = not is_raining
print(f"Is it dry? {is_dry}")  # False


# Example 4: Combined operators
age = 16
has_parent = True
can_watch_movie = (age >= 18) or (age >= 13 and has_parent)
print(f"Can watch movie: {can_watch_movie}")  # True (13+ with parent)


# Example 5: Short-circuit evaluation
def expensive_check():
    print("Expensive check executed")
    return True

value = False
result = value and expensive_check()  # expensive_check() never called
print(f"Result: {result}")  # False