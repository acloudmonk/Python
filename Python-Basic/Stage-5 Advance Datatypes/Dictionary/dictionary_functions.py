# clear() function
mydict = {"Name": "Ajay", "Age": 32, "Salary": 26000, "Company": "XYZ"}
print(mydict)
mydict.clear()
print(mydict)

# copy() function
mydict = {"Name": "Ajay", "Age": 32, "Salary": 26000, "Company": "XYZ"}
print(mydict)
mydict_new = mydict.copy()
print(mydict_new)

# fromkeys() function
mydict = {"Key1", "Key2", "Key3", "Key4", "Key5"}
result_dictionary = dict.fromkeys(mydict)
print(result_dictionary)

result_dictionary = dict.fromkeys(mydict, 10)
print(result_dictionary)

# get() function
mydict = {"Name": "Ajay", "Age": 32, "Salary": 26000, "Company": "XYZ"}
print(mydict.get("Name"))

# items() function
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
for x in numbers.items():
    print(x)

numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
for x, y in numbers.items():
    print(x, ":", y)

# keys() function
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
for x in numbers.keys():
    print(x, ":", numbers[x])

# pop() function
mydict = {"Name": "Ajay", "Age": 32, "Salary": 26000, "Company": "XYZ"}
print(mydict)
print(mydict.pop("Name"))
print(mydict)

# popitem() function
mydict = {"Name": "Ajay", "Age": 32, "Salary": 26000, "Company": "XYZ"}
print(mydict)
print(mydict.popitem())
print(mydict)

# setdefault() function
mydict = {"Name": "Ajay", "Age": 32}
print(mydict)
print(mydict.setdefault("Age", 30))
print(mydict)
print(mydict.setdefault("Salary", 26000))
print(mydict)
print(mydict.setdefault("Company", "XYZ"))
print(mydict)

# update() function
mydict = {"Name": "Ajay", "Age": 32}
otherdict = {"Salary": 26000, "Company": "XYZ"}
print(mydict)
print(otherdict)
mydict.update(otherdict)
print(mydict)

# values() function
mydict = {"Name": "Ajay", "Age": 32, "Salary": 26000, "Company": "XYZ"}
print(mydict.values())
