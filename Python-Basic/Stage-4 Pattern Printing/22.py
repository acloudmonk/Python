#     A
#    B C
#   D E F
#  G H I J
# K L M N O

rows = 5  # We can change the number of rows as needed
current_char = ord("A")
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print characters
    for k in range(i):
        print(chr(current_char), end=" ")
        current_char += 1
    print()
