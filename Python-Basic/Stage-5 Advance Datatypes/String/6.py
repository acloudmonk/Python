# Python program to remove duplicate characters from a string

# Method 1

# Get input string from user
user_input = input("Enter a string: ")
# Remove duplicate characters from the string
unique_chars = ""
for char in user_input:
    if char not in unique_chars:
        unique_chars += char
# Display the result
print("String without duplicate characters:", unique_chars)


# Method 2

# Get input string from user
user_input = input("Enter a string: ")
# Remove duplicate characters from the string
unique_chars = "".join(sorted(set(user_input), key=user_input.index))
# Display the result
print("String without duplicate characters:", unique_chars)
