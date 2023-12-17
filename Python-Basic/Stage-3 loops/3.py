# Enter a number and prints sum of all numbers upto that number

# using for loop
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num + 1):
    sum += i
print("The sum of numbers from 1 to", num, "is:", sum)

print("#####################")

# using while loop
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The sum of all numbers from 1 to", n, "is", sum)
