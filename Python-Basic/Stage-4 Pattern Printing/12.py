# 12345
#  2345
#   345
#    45
#     5

rows = 5  # We can change the number of rows as needed
for i in range(1, rows + 1):
    # Print spaces
    for j in range(1, i):
        print(" ", end="")
    # Print numbers
    for k in range(i, rows + 1):
        print(k, end="")
    print()
