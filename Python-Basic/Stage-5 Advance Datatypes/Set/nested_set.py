# below definition is wrong, it will give TypeError: unhashable type: 'set'
# example_set = {
#     {"apple", "banana", "guava"},
#     {"orange", "berry"},
#     {"cherry", "pineapple", "mango"},
#     {"papaya", "guava", "kiwi"},
# }

# Here's an example using tuples. In this example, the outer structure is a tuple
# containing sets as its elements. Tuples are immutable and, therefore, hashable,
# which makes them suitable for use in structures like sets.
nested_set = (
    {"apple", "banana", "guava"},
    {"orange", "berry"},
    {"cherry", "pineapple", "mango"},
    {"papaya", "guava", "kiwi"},
)

for single_set in nested_set:
    for single_item in single_set:
        print(single_item)

print("###############################")
# Here's an example using frozen set. Here, each inner set is a frozenset,
# which is an immutable and hashable variant of a set. This structure can be
# used as an element in another set.
nested_set = {
    frozenset({"apple", "banana", "guava"}),
    frozenset({"orange", "berry"}),
    frozenset({"cherry", "pineapple", "mango"}),
    frozenset({"papaya", "guava", "kiwi"}),
}

for single_set in nested_set:
    for single_item in single_set:
        print(single_item)
