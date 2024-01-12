# Python program to count even and odd number in given list

# Example list of numbers
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Initialize counters
even_count = 0
odd_count = 0

# Iterate through the list and count even and odd numbers
for num in number_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the results
print("Original List:", number_list)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
