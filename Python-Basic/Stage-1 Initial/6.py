# Prompt user to enter a character
character = input("Enter a character: ")

# Convert character to its ASCII code
ascii_code = ord(character)

# Print the result
print("The ASCII code of", character, "is", ascii_code)

# Prompt user to enter an ASCII code
ascii_code = int(input("Enter an ASCII code: "))

# Convert ASCII code to its corresponding character
character = chr(ascii_code)

# Print the result
print("The character corresponding to ASCII code", ascii_code, "is", character)
