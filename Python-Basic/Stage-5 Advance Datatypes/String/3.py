# Python program to check if given string is palindrome or not

# Get input string from user
user_input = input("Enter a string: ")

# Check if the cleaned string is equal to its reverse
if user_input == user_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
