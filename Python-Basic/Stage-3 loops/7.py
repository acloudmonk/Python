# Enter a more than one digit number and count number of digit.

# using for loop
num = input("Enter a number: ")
count = 0
for digit in num:
    count += 1
print("The number of digits is:", count)


# using while loop
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)


# using string manipulation
num = input("Enter a number: ")
digits = len(num)
print("Number of digits:", digits)
