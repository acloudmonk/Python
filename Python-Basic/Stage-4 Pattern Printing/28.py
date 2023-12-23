# 3 2 1 2 3
#  5 3 3 5
#   8 6 8
#   14 14
#     28

rows = 5  # We can change the number of rows as needed
row_list = [3, 2, 1, 2, 3]  # take initial row for logic

for i in range(rows):
    # print spaces
    for j in range(i):
        print(" ", end="")
    # print updated list
    for k in row_list:
        print(k, end=" ")
    # main logic where we are updating the
    # row_list with newly created values in temp_list
    temp_list = []
    for l in range(0, row_list.__len__() - 1):
        temp_list.append(row_list[l] + row_list[l + 1])
    row_list = temp_list
    print()
