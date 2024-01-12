# Python program to find numbers common in two lists.

# Example lists
list1 = [1, 2, 3, 4, 5, 8, 9]
list2 = [4, 6, 5, 7, 8]

# Find common numbers using a loop
common_numbers = [num for num in list1 if num in list2]

# Print the result
print("List 1:", list1)
print("List 2:", list2)
print("Common Numbers:", common_numbers)
