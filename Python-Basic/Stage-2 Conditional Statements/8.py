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
