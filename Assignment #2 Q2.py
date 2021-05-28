import math

base = input("Enter a base length of a right angle triangle: ")
height = input("Enter a height length of a right angle triangle: ")

area = float(base) * float(height) / 2

c_square = (float(base)**2 + float(height)**2)

c_length = math.sqrt(c_square)

perimeter = float(base) + float(height) + float(c_length)

print("The area of the triangle is", area, "the perimeter is", perimeter ,"the other length is",c_length,)

