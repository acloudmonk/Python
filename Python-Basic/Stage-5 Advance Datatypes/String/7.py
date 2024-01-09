# Python program to list unique characters with their count in a string

# Get input string from user
user_input = input("Enter a string: ")

# Create a dictionary to store character counts
char_counts = {}

# Count occurrences of each character in the string
for char in user_input:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

print(char_counts)
# Display unique characters and their counts
print("Unique characters and their counts:")
for char, count in char_counts.items():
    print(f"{char}: {count}")
