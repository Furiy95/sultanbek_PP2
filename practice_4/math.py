#example 1
import math

degrees = float(input("Input degree: "))

# Convert to radians (formula: radians = degrees * π / 180)
radians = degrees * math.pi / 180

print(f"Output radian: {radians:.6f}")

#example 2
# Formula: Area = (1/2) * (a + b) * h

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = 0.5 * (base1 + base2) * height

print(f"Expected Output: {area}")

#example 3
import math

# Formula: Area = (n * s²) / (4 * tan(π/n))

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is: {round(area)}")

#example 4
# Formula: Area = base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print(f"Expected Output: {area}")