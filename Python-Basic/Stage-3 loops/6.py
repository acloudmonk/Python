# Enter a number and check if that is isotonic number or not
# Example 6 = 3 + 2 + 1

# using for loop
num = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i
if sum_of_divisors == num:
    print(num, "is an isotonic number.")
else:
    print(num, "is not an isotonic number.")


# using while loop
num = int(input("Enter a number: "))
rem_sum = 0
temp = num
while temp > 0:
    rem = temp % 10
    rem_sum += rem
    temp //= 10
if num % rem_sum == 0:
    print(num, "is an isotonic number")
else:
    print(num, "is not an isotonic number")


# using list comprehension
num = int(input("Enter a number: "))
divisors = [i for i in range(1, num) if num % i == 0]
if sum(divisors) == num:
    print(num, "is an isotonic number.")
else:
    print(num, "is not an isotonic number.")
