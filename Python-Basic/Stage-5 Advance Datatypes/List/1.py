# Python program to find min, max number in a given number list

### Solution 1 ###
# Example list of numbers
number_list = [4, 2, 7, 1, 9, 5]

# Find minimum and maximum values
min_value = min(number_list)
max_value = max(number_list)

# Print the results
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")


### Solution 2 ###
# Example list of numbers
number_list = [4, 2, 7, 1, 9, 5]

# Find minimum and maximum values
sorted_list = sorted(number_list)
min_value = sorted_list[0]
max_value = sorted_list[-1]

# Print the results
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")


### Solution 3 ###
# Example list of numbers
number_list = [4, 2, 7, 1, 9, 5]

# Initialize min and max values with the first element of the list
min_value = max_value = number_list[0]

# Iterate through the list to find min and max
for num in number_list:
    if num < min_value:
        min_value = num
    elif num > max_value:
        max_value = num

# Print the results
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
