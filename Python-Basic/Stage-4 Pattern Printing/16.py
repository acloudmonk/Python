#     1
#    232
#   34543
#  4567654
# 567898765

rows = 5  # We can change the number of rows as needed
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print increasing numbers
    for k in range(i, i * 2):
        print(k, end="")
    # Print decreasing numbers
    for l in range(i * 2 - 2, i - 1, -1):
        print(l, end="")
    print()
