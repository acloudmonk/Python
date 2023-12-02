# there are different ways to swap two variables in Python. Here are a few examples:


print("############## Using a temporary variable ########################")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Before swapping: a =", a, "and b =", b)
# swap the values using a temporary variable
temp = a
a = b
b = temp
print("After swapping: a =", a, "and b =", b)


print("############## Using arithmetic operations #######################")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Before swapping: a =", a, "and b =", b)
# swap the values using arithmetic operations
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "and b =", b)


print("############## Using bitwise XOR operator ########################")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Before swapping: a =", a, "and b =", b)
# swap the values using bitwise XOR operator
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping: a =", a, "and b =", b)


print("############## Using tuple swapping ##############################")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Before swapping: a =", a, "and b =", b)
# swap the values
a, b = b, a
print("After swapping: a =", a, "and b =", b)

"""
The statement "a, b = b, a" in Python is called a tuple unpacking or tuple swapping.
The right-hand side creates a tuple (b, a), and the left-hand side unpacks the values
from this tuple into the variables a and b.
This results in the values of a and b being swapped.1
"""

print("############## tuple swapping with 4 variable ####################")
a = 10
b = 20
c = 30
d = 40
a, b, c, d = d, c, b, a
print("a =", a, "\nb =", b, "\nc =", c, "\nd =", d)
