# Enter two number and check if they are buddy pair numbers or not.
# examples of buddy pair number are 220 and 284
# sum of divisors of first number is equivalent to second number
# and sum of divisors of second number is equivalent to first number
# sum of divisors of 220 is 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
# sum of divisors of 284 is 1 + 2 + 4 + 71 + 142 = 220


# using for loop
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_of_first_number_divisors = 0
sum_of_second_number_divisors = 0

for i in range(1, num1):
    if num1 % i == 0:
        sum_of_first_number_divisors += i

for i in range(1, num2):
    if num2 % i == 0:
        sum_of_second_number_divisors += i

if sum_of_first_number_divisors == num2 and sum_of_second_number_divisors == num1:
    print("These are buddy pair numbers.")
else:
    print("These are not buddy pair numbers.")


# using while loop
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_of_first_number_divisors = 0
sum_of_second_number_divisors = 0

i = 1
while i < num1:
    if num1 % i == 0:
        sum_of_first_number_divisors += i
    i += 1

i = 1
while i < num2:
    if num2 % i == 0:
        sum_of_second_number_divisors += i
    i += 1

if sum_of_first_number_divisors == num2 and sum_of_second_number_divisors == num1:
    print("These are buddy pair numbers.")
else:
    print("These are not buddy pair numbers.")


# Using a function to find the sum of divisors and comparing the results
def sum_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if sum_divisors(num1) == num2 and sum_divisors(num2) == num1:
    print("These are buddy pair numbers.")
else:
    print("These are not buddy pair numbers.")


# Using a list comprehension to find the divisors and comparing the sums
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

divisors1 = [i for i in range(1, num1) if num1 % i == 0]
divisors2 = [i for i in range(1, num2) if num2 % i == 0]

if sum(divisors1) == num2 and sum(divisors2) == num1:
    print("These are buddy pair numbers.")
else:
    print("These are not buddy pair numbers.")
