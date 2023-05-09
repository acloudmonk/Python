# enter cost of book, if book cost is greater than 500 then provisde 10% discount otherwise print the net cost

# Prompt user to enter the cost of the book
cost = float(input("Enter the cost of the book: "))

# Calculate the net cost after applying discount if necessary
if cost > 500:
    discount = 0.1 * cost
    net_cost = cost - discount
    print("The net cost of the book is:", net_cost)
else:
    print("The net cost of the book is:", cost)
