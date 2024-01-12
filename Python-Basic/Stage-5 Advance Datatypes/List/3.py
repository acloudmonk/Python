# Python program to sort the numbers in a given number list

### Solution 1 ###
# Example list of numbers
number_list = [4, 2, 7, 1, 9, 5]

# Sort the list in ascending order
# we can sort in decending order if we will use reverse=True
sorted_list = sorted(number_list)

# Print the result
print("Original List:", number_list)
print("Sorted List:", sorted_list)


### Solution 2 ###
# Example list of numbers
number_list = [4, 2, 7, 1, 9, 5]

# Sort the list in ascending order (modifies the original list)
number_list.sort()

# Print the result
print("Sorted List:", number_list)
