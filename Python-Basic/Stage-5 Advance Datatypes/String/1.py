# Python program to find number of vowels and consonents in a given string.

# Get input string from user
user_input = input("Enter a string: ")

# Initialize counts
num_vowels = 0
num_consonants = 0

# Define vowels
vowels = "aeiouAEIOU"

# Loop through each character in the input string
for char in user_input:
    if char.isalpha():
        if char in vowels:
            num_vowels += 1
        else:
            num_consonants += 1

# Display the results
print("Number of vowels:", num_vowels)
print("Number of consonants:", num_consonants)
