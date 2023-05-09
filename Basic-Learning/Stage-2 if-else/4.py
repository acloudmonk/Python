# enter a salary of employee, if salary is greater than 10000 then add bonus 2000 otherwise 500 and then print net salary of employee

# Prompt user to enter the salary of the employee
salary = float(input("Enter the salary of the employee: "))

# Calculate the net salary after adding bonus if necessary
if salary > 10000:
    bonus = 2000
else:
    bonus = 500

net_salary = salary + bonus
print("The net salary of the employee is:", net_salary)
