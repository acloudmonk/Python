# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

rows = 5  # We can change the number of rows as needed
for i in range(1, rows + 1):
    for j in range(rows - i + 1, rows + 1):
        print(j, end=" ")
    print()
