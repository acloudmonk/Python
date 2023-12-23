# *********
# **** ****
# ***   ***
# **     **
# *       *
# **     **
# ***   ***
# **** ****
# *********

rows = 5  # We can change the number of rows as needed
# Print the top half
for i in range(rows):
    # Print asterisks on the left side
    for j in range(rows - i):
        print("*", end="")
    # Print spaces in the middle
    for k in range(2 * i):
        print(" ", end="")
    # Print asterisks on the right side
    for l in range(rows - i):
        print("*", end="")
    print()

# Print the bottom half
for i in range(rows):
    # Print asterisks on the left side
    for j in range(i + 1):
        print("*", end="")
    # Print spaces in the middle
    for k in range(2 * (rows - i - 1)):
        print(" ", end="")
    # Print asterisks on the right side
    for l in range(i + 1):
        print("*", end="")
    print()
