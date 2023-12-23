# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

rows = 5  # We can change the number of rows as needed
for i in range(1, rows + 1):
    num = i
    for j in range(i):
        print(num, end=" ")
        num += rows - (j + 1)
        # print(num)
    print()
