# we can also implement a small calculator using a dictionary in Python to map the user's input to the corresponding arithmetic operation.
# Here's an example program that uses a dictionary to implement a small calculator:


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


# Define a dictionary that maps the user's input to the corresponding arithmetic operation
operations = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide,
}

while True:
    # Display the menu and prompt the user for input
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter your choice: ")

    # Check the user's input and perform the corresponding operation
    if choice == "5":
        print("Exiting the program...")
        break
    elif choice in operations:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = operations[choice](num1, num2)
        print("The result is:", result)
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
