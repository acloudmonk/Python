# sum of two numbers
x = 5
y = 10
print("The sum of", x, "and", y, "is", x + y)

print("##### Using Input function #####")
x = input("Type a number: ")
y = input("Type another number: ")
# Add two numbers. input returns a string and we need to covert it to either int or float based on our need
sum = int(x) + int(y)
# Display the sum
print("The sum of {0} and {1} is {2}".format(x, y, sum))


# All operations in Single line. Although this program uses no variable (memory efficient), it is harder to read.
print("##### Use all statement in single line #####")
print(
    "The sum is %.1f"
    % (float(input("Enter first number: ")) + float(input("Enter second number: ")))
)
