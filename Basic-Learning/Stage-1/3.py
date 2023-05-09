# Enter radious of a circle and prints its area, parameter, diameter
import math

# Prompt user to enter radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area, perimeter, and diameter
area = math.pi * radius**2
perimeter = 2 * math.pi * radius
diameter = 2 * radius

# Print the results
print("The area of the circle is:", area)
print("The perimeter of the circle is:", perimeter)
print("The diameter of the circle is:", diameter)
