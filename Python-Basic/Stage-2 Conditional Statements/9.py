# here's a Python program that takes three numbers as input and prints the largest one:

##### Method 1: Using nested if-else statements #####
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 > num2:
    if num1 > num3:
        print("The largest number is:", num1)
    else:
        print("The largest number is:", num3)
else:
    if num2 > num3:
        print("The largest number is:", num2)
    else:
        print("The largest number is:", num3)


##### Method 2: Using if-else statements with logical operators #####
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number.")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number.")
else:
    print(num3, "is the largest number.")


##### Method 3: Using the max() function #####
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
largest = max(num1, num2, num3)
print("The largest number is:", largest)
