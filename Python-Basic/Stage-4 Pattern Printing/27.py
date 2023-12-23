# ******
#  *
#   *
#    *
#     *
# ******

rows = 5  # We can change the number of rows as needed
# Print the top row
print("*" * rows)
# Print the middle rows
for i in range(1, rows - 1):
    print(" " * i, end="")
    print("*")
# Print the bottom row
print("*" * rows)
