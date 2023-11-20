# Hello World Program

print("Hello World")

# Multi-line statement
item_one = 1
item_two = 2
item_three = 3
total = item_one + item_two + item_three
print(total)


# Statements contained within the [], {}, or () brackets do not need to use the line continuation character. For example following statement works well in Python
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Quotations
# The triple quotes are used to span the string across multiple lines. For example, all the following are legal
word = "word"
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
 made up of multiple lines and sentences."""

# Comments
# First comment
print("Hello, World!")  # Second comment
name = "Madisetti"  # This is again comment

# This is a comment.
# This is a comment, too.
# This is a comment, too.
# I said that already.

# Following triple-quoted string is also ignored by Python interpreter and can be used as a multiline comments:
"""
This is a multiline
comment.
"""

# Multiple Statements on a Single Line
# The semicolon ( ; ) allows multiple statements on the single line given that neither statement starts a new code block. Here is a sample snip using the semicolon
import sys

x = "foo"
sys.stdout.write(x + "\n")

# main function
# code without main function
print("How are you?")


def main():
    print("What about you?")


print("I am fine")
# code with main function
print("How are you?")


def main():
    print("What about you?")


print("I am fine")
if __name__ == "__main__":
    main()
