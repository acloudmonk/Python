# 567898765
#  4567654
#   34543
#    232
#     1

rows = 5  # We can change the number of rows as needed
for i in range(rows):
    # Print spaces
    for j in range(i):
        print(" ", end="")
    # Print decreasing numbers
    for k in range(rows - i, 2 * rows - 2 * i):
        print(k, end="")
    # Print decreasing numbers in reverse
    for l in range(2 * rows - 2 * i - 2, rows - (i + 1), -1):
        print(l, end="")
    print()
