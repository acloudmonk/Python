# ******
# *    *
# *    *
# *    *
# ******

rows = 5  # We can change the number of rows as needed
# Print the top row
print("*" * rows)
# Print the middle rows
for i in range(rows - 2):
    print("*", end="")
    print(" " * (rows - 2), end="")
    print("*")
# Print the bottom row
print("*" * rows)
