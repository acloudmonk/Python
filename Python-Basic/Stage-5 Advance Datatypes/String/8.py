# Python program to find number of words in a string

# Get input string from user
user_input = input("Enter a string: ")

# Split the string into words
words = user_input.split()

# Count the number of words
num_words = len(words)

# Display the result
print("Number of words in the string:", num_words)
