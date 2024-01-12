# Python program to create separate lists based on different datatype present in the list.

# Example list with different data types
mixed_list = [1, "apple", 2.5, "banana", True, 3, "kiwi", False]

# Initialize a dictionary to store lists based on data types
type_lists = {}

# Iterate through the mixed list and categorize elements
for item in mixed_list:
    data_type = type(item).__name__  # Get the name of the data type
    if data_type not in type_lists:
        type_lists[data_type] = []  # Create a new list for the data type if not exists
    type_lists[data_type].append(item)  # Append the item to the corresponding list

# Print the results
print("Original List:", mixed_list)
for data_type, items in type_lists.items():
    print(f"{data_type.capitalize()}s List:", items)
