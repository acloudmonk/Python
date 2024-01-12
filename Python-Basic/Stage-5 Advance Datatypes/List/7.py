# Python program to find unique numbers in a given list

### Solution 1 ###

# Example list of numbers
number_list = [1, 2, 3, 2, 4, 5, 1, 6, 7, 3, 8, 9, 5]

# Find unique numbers using a set
unique_numbers = list(set(number_list))

# Print the result
print("Original List:", number_list)
print("Unique Numbers:", unique_numbers)


### Solution 2 ###

# Example list of numbers
number_list = [1, 2, 3, 2, 4, 5, 1, 6, 7, 3, 8, 9, 5]

# Find unique numbers while preserving order
unique_numbers = []
for num in number_list:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Print the result
print("Original List:", number_list)
print("Unique Numbers (Preserving Order):", unique_numbers)
