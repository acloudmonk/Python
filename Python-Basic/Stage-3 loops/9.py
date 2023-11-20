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


# using recursion
def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sum_of_digits(num // 10)


num = int(input("Enter a more than one digit number: "))
print("Sum of digits:", sum_of_digits(num))
