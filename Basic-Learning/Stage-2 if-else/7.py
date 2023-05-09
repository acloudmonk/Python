# Enter a basic salary of employee and prints net salary which includes DA, HRA, TA based on certain conditions.
# if salary > 20000, DA=10%, HRA=8%, TA=6%
# if salary > 15000, DA=8%, HRA=6%, TA=4%
# if salary > 10000, DA=6%, HRA=4%, TA=2%

basic_salary = float(input("Enter basic salary: "))
if basic_salary > 20000:
    DA = 0.1 * basic_salary
    HRA = 0.08 * basic_salary
    TA = 0.06 * basic_salary
elif basic_salary > 15000:
    DA = 0.08 * basic_salary
    HRA = 0.06 * basic_salary
    TA = 0.04 * basic_salary
elif basic_salary > 10000:
    DA = 0.06 * basic_salary
    HRA = 0.04 * basic_salary
    TA = 0.02 * basic_salary
else:
    DA = 0
    HRA = 0
    TA = 0

net_salary = basic_salary + DA + HRA + TA
print("Net Salary:", net_salary)
