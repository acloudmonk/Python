number = int(input("Enter Any-digit number: "))
result=0
a = number
while a>0:
    result = result*10 + a%10
    a = a/10
print(number)
print(result)
if (number == result):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
