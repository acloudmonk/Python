# 1
# 6 5
# 11 10 9
# 16 15 14 13
# 21 20 19 18 17

rows = 5  # We can change the number of rows as needed
current_num = 1
for i in range(1, rows + 1):
    # Print numbers
    for j in range(current_num, current_num - i, -1):
        print(j, end=" ")
    current_num += 5
    print()
