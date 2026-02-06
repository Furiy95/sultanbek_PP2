# Example 1: Equality comparison
age = 25
is_adult = (age >= 18)
print(f"Age {age} is adult: {is_adult}")  # True
print(f"Age equals 25: {age == 25}")      # True

# Example 2: String comparison
name1 = "Alice"
name2 = "Bob"
print(f"Names equal: {name1 == name2}")       # False
print(f"Alice < Bob alphabetically: {name1 < name2}")  # True

# Example 3: Floating point comparison
pi = 3.14159
user_pi = 3.14
print(f"Pi equals user input: {pi == user_pi}")        # False
print(f"Pi greater than user input: {pi > user_pi}")   # True

# Example 4: Multiple comparisons
temperature = 72
is_comfortable = (65 <= temperature <= 75)
print(f"Temperature {temperature} is comfortable: {is_comfortable}")  # True

# Example 5: Identity comparison with `is`
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(f"a == b: {a == b}")    # True (same values)
print(f"a is b: {a is b}")    # False (different objects)
print(f"a is c: {a is c}")    # True (same object)