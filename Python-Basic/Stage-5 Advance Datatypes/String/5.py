# Python program to drop all digits from a string

# Method 1

# Get input string from user
user_input = input("Enter a string: ")
# Drop all digits from the string
result_string = ""
for char in user_input:
    if not char.isdigit():
        result_string += char
# Display the result
print("String without digits:", result_string)

# Method 2

# Get input string from user
user_input = input("Enter a string: ")
# Drop all digits from the string
result_string = "".join(char for char in user_input if not char.isdigit())
# Display the result
print("String without digits:", result_string)
