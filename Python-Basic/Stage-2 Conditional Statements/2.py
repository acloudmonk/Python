# enter a year and check if that is leap year or not

# Prompt user to enter a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
