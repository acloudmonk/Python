# Enter a more than one digit number and prints sum of digits.


# using for loop
num = input("Enter a more than one digit number: ")
sum = 0
for digit in num:
    sum += int(digit)
print("Sum of digits:", sum)


# using while loop
num = int(input("Enter a more than one digit number: "))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print("Sum of digits:", sum)
