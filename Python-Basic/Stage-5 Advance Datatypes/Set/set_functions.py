example_set1 = {"apple", "banana", "guava"}
example_set1.add("orange")
print(example_set1)

# update() method inserts the items in example_set2 into example_set1
example_set2 = {"cherry", "pineapple", "mango", "papaya"}
example_set1.update(example_set2)
print(example_set1)

# update() method inserts the items in example_list into example_set1
example_list = ["kiwi", "berry"]
example_set1.update(example_list)  # list updated in set
print(example_set1)

example_set1.remove("kiwi")  # raise error if value does not exist
print(example_set1)

example_set1.discard("cherry")  # discard will not raise error if value does not exist
print(example_set1)

removed_item = example_set1.pop()
print(removed_item)
print(example_set1)

example_set2.clear()
print(example_set2)

example_set1 = {1, 2, 3, 4}
# copies the items of example_set1 to example_set2
example_set1 = example_set1.copy()
print(example_set1)
print(example_set2)

example_set1 = {"apple", "banana", "guava", "orange", "berry"}
example_set2 = {"cherry", "pineapple", "mango", "papaya", "guava", "kiwi"}

# union() method returns a new set containing all items from both sets
example_set3 = example_set1.union(example_set2)
print(example_set3)

example_set1 = {"apple", "banana", "guava", "orange", "berry", "mango"}
example_set2 = {"cherry", "pineapple", "mango", "papaya", "guava", "kiwi"}

# intersection_update() method will keep only the items that are present in both sets
example_set1.intersection_update(example_set2)
print(example_set1)

example_set1 = {"apple", "banana", "guava", "orange", "berry", "mango"}
example_set2 = {"cherry", "pineapple", "mango", "papaya", "guava", "kiwi"}

# intersection() method will return a new set
# which will contains the items that are present in both sets
example_set3 = example_set1.intersection(example_set2)
print(example_set3)

# intersection_update() method will update example_set1 with items
# which are common in both sets
example_set1.intersection_update(example_set2)
print(example_set3)

example_set1 = {"guava", "orange", "berry", "mango"}
example_set2 = {"mango", "papaya", "guava", "kiwi"}
# Return a set that contains the items that only exist in calling object
example_set3 = example_set1.difference(example_set2)
print(example_set3)

example_set1 = {"guava", "orange", "berry", "mango"}
example_set2 = {"mango", "papaya", "guava", "kiwi"}
# symmetric_difference_update() method will keep only the elements
# which are NOT present in both sets
example_set1.symmetric_difference_update(example_set2)
print(example_set1)

example_set1 = {"guava", "orange", "berry", "mango"}
example_set2 = {"mango", "papaya", "guava", "kiwi"}

# symmetric_difference() method will return a new set
# which will contains only the elements that are NOT present in both sets
example_set3 = example_set1.symmetric_difference(example_set2)
print(example_set3)

example_set1 = {"guava", "orange", "berry", "mango"}
example_set2 = {"mango", "papaya", "guava", "kiwi"}
print(example_set1.isdisjoint(example_set2))
print(example_set1.issubset(example_set2))
print(example_set1.issuperset(example_set2))
