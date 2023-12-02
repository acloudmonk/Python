# Small calculator program
# Menu
# 1. Add
# 2. Substract
# 3. Multiply
# 4. Devide
# 5. Exit
# Enter your input :

print("Menu\n1. Add\n2. Substract\n3. Multiply\n4. Devide\n5. Exit\n")

# Display the menu and prompt the user for input

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
    exit()
else:
    print("Invalid choice! Please enter a number between 1 and 5.")
