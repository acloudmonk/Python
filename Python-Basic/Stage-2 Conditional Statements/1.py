# enter a number and print if that is even number or odd

# Prompt user to enter a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")


# Prompt user to enter a number
number = int(input("Enter a number: "))

# Check if the number is even or odd using divmod
quo, rem = divmod(number, 2)

if rem == 0:
    print(number, "is even")
else:
    print(number, "is odd")
