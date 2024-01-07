# Python program to reverse the string provided.

# Method 1

# Get input string from user
user_input = input("Enter a string: ")
# Reverse the string
reversed_string = user_input[::-1]
# Display the reversed string
print("Reversed string:", reversed_string)

# Method 2

# Get input string from user
user_input = input("Enter a string: ")
# Reverse the string using reversed() function
reversed_string = "".join(reversed(user_input))
# Display the reversed string
print("Reversed string:", reversed_string)

# Method 3

# Get input string from user
user_input = input("Enter a string: ")
# Initialize an empty string to store the reversed string
reversed_string = ""
# Iterate through each character in the input string in reverse order
for char in reversed(user_input):
    reversed_string += char
# Display the reversed string
print("Reversed string:", reversed_string)
