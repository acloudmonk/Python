# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

rows = 5  # We can change the number of rows as needed
counter = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(counter, end=" ")
        counter += 1
    print()
