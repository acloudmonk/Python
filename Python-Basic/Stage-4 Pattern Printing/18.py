#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

rows = 5  # We can change the number of rows as needed
for i in range(rows):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print coefficients
    coeff = 1
    for k in range(i + 1):
        print(coeff, end=" ")
        coeff = coeff * (i - k) // (k + 1)
    print()
