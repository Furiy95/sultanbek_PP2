# Example 1: Basic boolean values
is_sunny = True
is_raining = False
print(f"Sunny: {is_sunny}, Raining: {is_raining}")
print(f"Type of is_sunny: {type(is_sunny)}")  # <'bool'>

# Example 2: 
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Example 3: Numeric boolean conversion
zero = 0
non_zero = 42
print(f"bool(0): {bool(zero)}")        # False
print(f"bool(42): {bool(non_zero)}")   # True

# Example 4: None as a boolean
none_value = None
print(f"bool(None): {bool(none_value)}")  # False

# Example 5: Automatic boolean conversion in conditions
value = 100
if value:  # Automatically converts to bool
    print("Value is truthy")  # Executes
else:
    print("Value is falsy")