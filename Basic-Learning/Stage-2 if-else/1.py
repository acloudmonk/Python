# enter a number and print if that is even number or odd

# Prompt user to enter a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# there is another way to check if a number is even or odd in Python.
# You can use the bitwise AND operator (&) with the number 1 to check its last bit.
# If the last bit is 0, the number is even; if it's 1, the number is odd.
# Here's an example code that demonstrates this approach:

# Prompt user to enter a number
number = int(input("Enter a number: "))

# Check if the number is even or odd using bitwise AND
if number & 1 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Explanation:
# We first prompt the user to enter a number using the input() function.
# We convert the input string to an integer using the int() function and store it in the number variable.

# We then use an if statement to check whether the number is even or odd using bitwise AND.
# We do this by performing a bitwise AND operation between the number and 1 (which has a binary representation of 00000001).
# This operation preserves only the last bit of the number, which is 0 for even numbers and 1 for odd numbers.

# If the last bit is 0, the number is even, so we print a message that says so using the print() function.
# We use the + operator to concatenate the value of number with the string "is even".

# If the last bit is 1, the number is odd, so we print a message that says so using the print() function.
# We use the + operator to concatenate the value of number with the string "is odd".

# Prompt user to enter a number
number = int(input("Enter a number: "))

# Check if the number is even or odd using divmod
quo, rem = divmod(number, 2)

if rem == 0:
    print(number, "is even")
else:
    print(number, "is odd")
