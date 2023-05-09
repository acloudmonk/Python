# there are different ways to swap two variables in Python. Here are a few examples:

# Here's the Python code to swap two numbers:
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("Before swapping: a =", a, "and b =", b)
# swap the values
a, b = b, a
print("After swapping: a =", a, "and b =", b)


# Using a temporary variable:
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("Before swapping: a =", a, "and b =", b)
# swap the values using a temporary variable
temp = a
a = b
b = temp
print("After swapping: a =", a, "and b =", b)


# Using arithmetic operations:
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("Before swapping: a =", a, "and b =", b)
# swap the values using arithmetic operations
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "and b =", b)


# Using bitwise XOR operator:
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("Before swapping: a =", a, "and b =", b)
# swap the values using bitwise XOR operator
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping: a =", a, "and b =", b)
