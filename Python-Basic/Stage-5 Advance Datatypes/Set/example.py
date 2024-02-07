example_set1 = {"apple", "banana", "cherry", "apple"}
example_set2 = {"sachin", 2024, True, 40, "ramesh"}
print(example_set1)
print(example_set2)

# We can also use the set() constructor to make a set
example_set3 = set(("sachin", 2024, True, 40, "ramesh"))
print(example_set3)

# some other examples of set() constructor
print(set())  # empty set
print(set("Sachin"))  # from string
print(set(("apple", "banana", "cherry")))  # from tuple
print(set(["apple", "banana", "cherry"]))  # from list
print(set(range(5)))  # from range
print(set({"a", "e", "i", "o", "u"}))  # from set
print(set({"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}))  # from dictionary
frozen_set = frozenset(("a", "e", "i", "o", "u"))  # from frozen set
print(set(frozen_set))

# check set length and type
print(len(example_set3))
print(type(example_set3))
