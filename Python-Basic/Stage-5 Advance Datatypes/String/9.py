# Python program to remove all non-alphabetic characters from a string

# Method 1

# Get input string from user
user_input = input("Enter a string: ")
# Remove all non-alphabetic characters from the string
alpha_chars = ""
for char in user_input:
    if char.isalpha():
        alpha_chars += char
# Display the result
print("String with only alphabetic characters:", alpha_chars)

# Method 2

# Get input string from user
user_input = input("Enter a string: ")
# Remove all non-alphabetic characters from the string
alpha_chars = "".join(char for char in user_input if char.isalpha())
# Display the result
print("String with only alphabetic characters:", alpha_chars)
