# format() function
print("Ramesh scored {} out of {} marks.".format(80, 100))
print("Ramesh scored {1} out of {0} marks.".format(80, 100))
print("Ramesh scored {first} out of {second} marks.".format(first="80", second="100"))

# format_map() function
print("My {x} is {y} USD".format_map({"x": "Salary", "y": 8700}))
detail = {
    "name": ["Sachin", "Viman"],
    "profession": ["Architect", "Businessman"],
    "age": [34, 29],
}

print(
    "{name[0]} is an {profession[0]} and he" " is {age[0]} years old".format_map(detail)
)

print(
    "{name[1]} is a {profession[1]} and he" " is {age[1]} years old".format_map(detail)
)

# strip(), lstrip() and rstrip() functions
print("     Hello       " + "World")
print("     Hello       ".strip() + "World")
print("     Hello       ".lstrip() + "World")
print("     Hello       ".rstrip() + "World")

# lower(), upper(), casefold(), title(), capitalize() and swapcase() functions
print("Hello World".lower())
print("Hello World".upper())
print("Hello World".casefold())
print("hello world".title())
print("hello world".capitalize())
print("Hello World".swapcase())

# split() rsplit() function
print("Hello Cloud Monks".split())
print(
    "Hello Cloud Monks, My name is Sachin Singh, Your are wathing 'A Cloud Monk' youtube channel".split(
        ", "
    )
)
print("Potato#Tomato#Brinjal#Onion".split("#"))
print("Potato#Tomato#Brinjal#Onion".split("#", 1))

print("Hello Cloud Monks".rsplit())
print(
    "Hello Cloud Monks, My name is Sachin Singh, Your are wathing 'A Cloud Monk' youtube channel".rsplit(
        ", "
    )
)
print("Potato#Tomato#Brinjal#Onion".rsplit("#"))
print("Potato#Tomato#Brinjal#Onion".rsplit("#", 1))

print(
    "Hello Cloud Monks\nMy name is Sachin Singh\nYour are wathing 'A Cloud Monk' youtube channel".splitlines()
)

# find(), rfind(), index() and rindex() functions
print("Hello Cloud Monks".find("Cloud"))
print("Potato#Tomato#Brinjal#Onion".find("#"))
print("Potato#Tomato#Brinjal#Onion".find("#", 10, 25))
print("Hello Cloud Monks".find("Alpha"))

print("Hello Cloud Monks".rfind("Cloud"))
print("Potato#Tomato#Brinjal#Onion".rfind("#"))
print("Potato#Tomato#Brinjal#Onion".rfind("#", 10, 25))
print("Hello Cloud Monks".rfind("Alpha"))

print("Hello Cloud Monks".index("Cloud"))
print("Potato#Tomato#Brinjal#Onion".index("#"))
print("Potato#Tomato#Brinjal#Onion".index("#", 10, 25))
# print("Hello Cloud Monks".index("Alpha"))

print("Hello Cloud Monks".rindex("Cloud"))
print("Potato#Tomato#Brinjal#Onion".rindex("#"))
print("Potato#Tomato#Brinjal#Onion".rindex("#", 10, 25))
# print("Hello Cloud Monks".rindex("Alpha"))

# count() function
print("Hello Cloud Monks".count("Cloud"))
print("Potato#Tomato#Brinjal#Onion".count("#"))
print("Potato#Tomato#Brinjal#Onion".count("#", 10, 25))
print("Hello Cloud Monks".count("Alpha"))

# maketrans() and translate() functions
# maketrans() and translate() functions
text = "Bello Gloud Monks!"
mytable = str.maketrans("BG", "HC")
print(text.translate(mytable))
mytable = str.maketrans("BG", "HC", "s")
print(text.translate(mytable))

# startswith() and endswith() functions
print("Hello Cloud Monks".startswith("Cloud"))
print("Hello Cloud Monks".startswith("Hello"))
print("Hello Cloud Monks".startswith("Cloud", 6, 20))
print("Hello Cloud Monks".startswith("Hello", 6, 20))

print("Hello Cloud Monks".endswith("Cloud"))
print("Hello Cloud Monks".endswith("Monks"))
print("Hello Cloud Monks".endswith("Cloud", 0, 11))
print("Hello Cloud Monks".endswith("Monks", 0, 11))

# replace() function
print("Hello Cloud Monks".replace("Cloud", "World"))
print("Hello Cloud Monks".replace("o", "a", 2))

# join() function
myTuple = ("Hello", "Cloud", "Monks")
print("#".join(myTuple))
myDict = {"fname": "Sachin", "lname": "Singh"}
print(",".join(myDict))
myList = ["My", "Name", "is", "Sachin", "Singh"]
print(" ".join(myList))

# encode() function
print("My name is Såchin".encode())

# expandtabs() function
message = "H\te\tl\tl\to\tCloudMonks"
print(message)
print(message.expandtabs(2))

# center(), ljust() and rjust() functions
text = "A Cloud Monk"
print(text.center(100))
print(text.center(100, "_"))
print(text.ljust(100, "_"))
print(text.rjust(100, "_"))

# partition() and rpartition() functions
text = "I love to hear cloud monks"
print(text.partition("o"))
print(text.rpartition("o"))

# removeprefix() and removesuffix() functions
text = "Hello Cloud Monks"
print(text.removeprefix("Hello"))
print(text.removesuffix("Monks"))

# zfill() function
text = "Hello Cloud Monks"
print(text.zfill(20))
print(text.zfill(10))
print(text.zfill(30))
