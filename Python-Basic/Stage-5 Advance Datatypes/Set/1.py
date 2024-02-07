# Python program to find numbers common in two lists.

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find common numbers using set intersection
common_numbers = list(set(list1) & set(list2))

# Print the result
print("List 1:", list1)
print("List 2:", list2)
print("Common Numbers:", common_numbers)
