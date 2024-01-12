# Python program to count the occurrences of a list item.

# Example list of numbers
number_list = [1, 2, 3, 2, 4, 5, 2, 6, 7, 2, 3, 7, 3, 1]

# Dictionary to store item occurrences
occurrences_dict = {}

# Count occurrences for each item
for item in number_list:
    if item in occurrences_dict:
        occurrences_dict[item] += 1
    else:
        occurrences_dict[item] = 1

# Print the results
for item, count in occurrences_dict.items():
    print(f"Occurrences of {item}: {count}")
