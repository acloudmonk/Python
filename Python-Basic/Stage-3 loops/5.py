# Enter a number and prints table of that number

# using a for loop
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# using while loop
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

# Using a list comprehension
num = int(input("Enter a number: "))
table = [num * i for i in range(1, 11)]
for t in table:
    print(str(num) + " * " + str(int(t / num)) + " = " + str(t))
