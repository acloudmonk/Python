# Python program to create a list of 5 random integers
import random

# Generate a list of 5 random integers
random_integers = [random.randint(1, 100) for _ in range(5)]

# Print the result
print("Random Integers:", random_integers)
