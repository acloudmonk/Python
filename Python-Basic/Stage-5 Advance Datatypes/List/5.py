# Python program to compare two list and tell if both are equal or not

### Solution 1 ###

# Example lists
list1 = [1, 9, 3, 4, 5]
list2 = [1, 5, 3, 4, 9]

# Check if both lists are equal using sorted()
if sorted(list1) == sorted(list2):
    print("Both lists are equal.")
else:
    print("The lists are not equal.")


list1 = [1, 5, 3, 4, 9]
list2 = [1, 4, 3, 5, 9]
if list1 == list2:
    print("Both lists are equal.")
else:
    print("The lists are not equal.")
