# 15 14 13 12 11
# 10 9 8 7
# 6 5 4
# 3 2
# 1

rows = 5  # We can change the number of rows as needed
counter = 15
for i in range(rows, 0, -1):
    for j in range(i):
        print(counter, end=" ")
        counter -= 1
    print()
