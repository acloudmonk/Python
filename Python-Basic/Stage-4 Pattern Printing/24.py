# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

rows = 5  # You can change the number of rows as needed
for i in range(rows):
    # Initialize the first element in the row
    current_num = 1
    # Print numbers
    for j in range(i + 1):
        print(current_num, end=" ")
        # Calculate the next element using the binomial coefficient
        current_num = current_num * (i - j) // (j + 1)
    print()
