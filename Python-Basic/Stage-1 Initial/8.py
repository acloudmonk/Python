# Enter a number and its power and prints the result

##### Solution - First #####

# Prompt user to enter a number
number = float(input("Enter a number: "))
# Prompt user to enter the power
power = int(input("Enter the power: "))
# Calculate the result
result = number**power
# Print the result
print(number, "to the power of", power, "is", result)

##### Solution - Second #####

# Prompt user to enter a number
number = float(input("Enter a number: "))
# Prompt user to enter the power
power = int(input("Enter the power: "))
# Calculate the result
result = pow(number, power)
# Print the result
print(number, "to the power of", power, "is", result)
