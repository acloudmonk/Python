# Enter a more than one digit number and prints reverse of that number.


# using for loop
num = input("Enter a more than one digit number: ")
reverse_num = ""
for i in range(len(num) - 1, -1, -1):
    reverse_num += num[i]
print("Reverse of the number:", reverse_num)


# using while loop
num = int(input("Enter a more than one digit number: "))
reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10
print("Reverse of the number:", reverse_num)


# Using string slicing and concatenation
num = input("Enter a more than one digit number: ")
reverse_num = num[::-1]
print("Reverse of the number:", reverse_num)
