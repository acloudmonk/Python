# enter a year and check if that is leap year or not
# A year is a leap year if it is divisible by 4.
# 2022However, if the year is divisible by 100, it is not a leap year unless it is also divisible by 400.

# Prompt user to enter a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
