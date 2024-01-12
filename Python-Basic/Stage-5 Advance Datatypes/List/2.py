# Python program to remove duplicate items from the list

### Solution 1 ###
# Example list with duplicates
original_list = [1, 2, 3, 2, 4, 5, 6, 1, 7]

# Remove duplicates using a set
unique_list = list(set(original_list))

# Print the result
print("Original List:", original_list)
print("List with Duplicates Removed:", unique_list)


### Solution 2 ###
# Example list with duplicates
original_list = [1, 2, 3, 2, 4, 5, 6, 1, 7]

# Remove duplicates while preserving order
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

# Print the result
print("Original List:", original_list)
print("List with Duplicates Removed:", unique_list)
