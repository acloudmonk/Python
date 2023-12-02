# Here's an example program that implements a small calculator using a while loop and an if-elif-else statement to handle the user's input:

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
    if choice == "1":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print("The result is:", result)
    elif choice == "2":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print("The result is:", result)
    elif choice == "3":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print("The result is:", result)
    elif choice == "4":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("The result is:", result)
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
