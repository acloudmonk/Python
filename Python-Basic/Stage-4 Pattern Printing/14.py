#     1
#    12
#   123
#  1234
# 12345
#  1234
#   123
#    12
#     1

rows = 5  # We can change the number of rows as needed
# Print the first half
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print numbers
    for k in range(1, i + 1):
        print(k, end="")
    print()

# Print the second half
for i in range(rows - 1, 0, -1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print numbers
    for k in range(1, i + 1):
        print(k, end="")
    print()
