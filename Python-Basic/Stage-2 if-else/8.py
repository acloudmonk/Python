# here's a Python program that checks if a four-digit number is a palindrome or not:
# examples are 2332, 1221 etc.

##### First #####
number = int(input("Enter a four-digit number: "))
# Extract each digit of the number
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
units = number % 10
# Check if the number is a palindrome
if thousands == units and hundreds == tens:
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome.")


##### Second #####
# It checks if the number is equal to its reverse (number[::-1]) using string slicing.
# If the number is equal to its reverse, then it is a palindrome.

# Note that in this program, the user input is treated as a string rather than an integer.
# This allows us to easily reverse the string using slicing.
number = input("Enter a four-digit number: ")
if number == number[::-1]:
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome.")
