# 1
# 4 9
# 16 25 36
# 49 64 81 100
# 121 144 169 196 225

rows = 5  # We can change the number of rows as needed
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num**2, end=" ")
        num += 1
    print()
