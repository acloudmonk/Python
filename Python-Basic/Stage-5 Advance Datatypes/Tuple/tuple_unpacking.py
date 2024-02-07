tuple_original = ("Sachin", "Cloud", 35, 99.99)

# without unpacking
first_value = tuple_original[0]
second_value = tuple_original[1]
third_value = tuple_original[2]
fourth_value = tuple_original[3]

# with tuple unpacking and variable should be same as values in the list
first, second, third, fourth = tuple_original
print(first, second, third, fourth)

# with tuple unpacking and variable can be less if using list as variable
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first, second, *other = numbers
print(first, second, other)
first, *other, last = numbers
print(first, last, other)
