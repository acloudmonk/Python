# Enter a number and check if that is armstrong number or not. Example 153 = 1**3+5**3+3**3

# using for loop
num = int(input("Enter a number: "))
sum = 0
for digit in str(num):
    sum += int(digit) ** 3
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# using while loop
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# using list comprehension
num = int(input("Enter a number: "))
sum = sum([int(digit) ** 3 for digit in str(num)])
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
