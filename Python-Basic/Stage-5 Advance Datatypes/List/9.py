# Python program to sort a list of strings on the number of alphabets in each word.

# Example list of strings
string_list = ["apple", "The", "banana", "kiwi", "An", "orange", "grape", "A"]


# Custom function to calculate the number of alphabets in a word
def alphabet_count(word):
    return sum(c.isalpha() for c in word)


# Sort the list based on the number of alphabets in each word
sorted_list = sorted(string_list, key=alphabet_count)

# Print the result
print("Original List:", string_list)
print("Sorted List by Alphabet Count:", sorted_list)
