import math

# 1 circumference of a circle
radius = int(input("Enter the radius of the circle: "))
circumference = 2 * 3.14159 * radius
# print(f"The circumference of the circle is: {circumference}")

# 2 area of a circle
area = 3.14159* radius * radius
print(f"The area of the circle is: {area}")


# 3 hypotenious of a triangle
a = int(input("Enter the first value"))
b = int(input("Enter the second value"))
c = pow(a,2) + pow(b,2)
print(math.sqrt(c))
# print(math.sqrt(a*a + b*b))