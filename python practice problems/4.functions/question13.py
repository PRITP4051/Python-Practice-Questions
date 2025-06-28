#WAP to determine sine, cosine and tangent of a given number.
import math

num = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
radians = math.radians(num)

sine = math.sin(radians)
cosine = math.cos(radians)
tangent = math.tan(radians)

print(f"Sine of {num}° is {sine}")
print(f"Cosine of {num}° is {cosine}")
print(f"Tangent of {num}° is {tangent}")