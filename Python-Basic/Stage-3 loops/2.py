# Enter two numbers and prints all even numbers which comes between these numbers

# using for loop
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)

# using while loop
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    num1, num2 = num2, num1  # swap the numbers if they are entered in descending order
print("Even numbers between", num1, "and", num2, "are:")
while num1 <= num2:
    if num1 % 2 == 0:
        print(num1)
    num1 += 1
