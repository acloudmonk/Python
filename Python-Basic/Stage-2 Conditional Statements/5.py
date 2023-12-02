# Here's an example code that prompts the user to enter two numbers and an arithmetic operator, performs the operation and prints the result:

# Method 1 : by using if elif else condition
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


# Method 2 : by using match case condition
# Prompt user to enter two numbers and an arithmetic operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the arithmetic operator (+, -, *, /): ")

# Perform the operation based on the operator entered by the user
match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2
    case default:
        print("Invalid operator entered!")
        exit()

# Print the result of the operation
print("The result of the operation is:", result)
