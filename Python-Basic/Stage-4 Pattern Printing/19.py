# 1
# 1 1
# 1 1 2
# 1 1 2 3
# 1 1 2 3 5
# 1 1 2 3 5 8
# 1 1 2 3 5 8 13

rows = 7  # We can change the number of rows as needed
fib_sequence = [1, 1]
for i in range(1, rows + 1):
    for num in fib_sequence[:i]:
        print(num, end=" ")
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print()
