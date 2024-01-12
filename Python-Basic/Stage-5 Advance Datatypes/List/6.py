# Python program to sum of all number in given number list

### Solution 1 ###

# Example list of numbers
number_list = [1, 2, 3, 4, 5]

# Calculate the sum of all numbers
sum_of_numbers = sum(number_list)

# Print the result
print(f"Sum of all numbers: {sum_of_numbers}")


### Solution 2 ###


# Example list of numbers
number_list = [1, 2, 3, 4, 5]

# Calculate the sum of all numbers using a loop
sum_of_numbers = 0
for num in number_list:
    sum_of_numbers += num

# Print the result
print(f"Sum of all numbers: {sum_of_numbers}")
