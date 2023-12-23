# 12345654321
# 12345 54321
# 1234   4321
# 123     321
# 12       21
# 1         1

rows = 6  # We can change the number of rows as needed
for i in range(rows):
    # Print increasing numbers
    for j in range(1, rows - i + 1):
        print(j, end="")
    # Print spaces
    for k in range(1, 2 * i):
        print(" ", end="")
    # Print decreasing numbers
    for l in range(rows - i, 0, -1):
        print(l, end="")
    print()
