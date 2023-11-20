# Here's an example code that prompts the user to enter two numbers and an arithmetic operator, performs the operation and prints the result:

# Prompt user to enter two numbers and an arithmetic operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the arithmetic operator (+, -, *, /): ")

# Perform the operation based on the operator entered by the user
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator entered!")
    exit()

# Print the result of the operation
print("The result of the operation is:", result)

# Python does not have a built-in switch-case statement like some other programming languages, but we can simulate it using a dictionary.
# Here's an example code that prompts the user to enter two numbers and an arithmetic operator,
# performs the operation using a switch-case equivalent implementation using a dictionary, and prints the result:

# Define a dictionary that maps the operator to the corresponding function
ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

# Prompt user to enter two numbers and an arithmetic operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the arithmetic operator (+, -, *, /): ")

# Perform the operation based on the operator entered by the user
if operator in ops:
    result = ops[operator](num1, num2)
else:
    print("Invalid operator entered!")
    exit()

# Print the result of the operation
print("The result of the operation is:", result)
