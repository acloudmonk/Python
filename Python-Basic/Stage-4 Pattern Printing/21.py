# 1       1
# 12     21
# 123   321
# 1234 4321
# 123454321

rows = 5  # We can change the number of rows as needed
for i in range(1, rows + 1):
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    # Print spaces
    for k in range(2 * (rows - i) - 1):
        print(" ", end="")
    # Print decreasing numbers
    for l in range(i, 0, -1):
        if l != 5:
            print(l, end="")
    print()
