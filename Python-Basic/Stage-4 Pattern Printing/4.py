# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

rows = 5  # We can change the number of rows as needed
for i in range(1, rows + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
