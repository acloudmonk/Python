# Enter temparature in farenhite and change in centigrate and print it

# Prompt user to enter temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Print the result
print(
    "{:.2f} degrees Fahrenheit is equal to {:.2f} degrees Celsius".format(
        fahrenheit, celsius
    )
)
