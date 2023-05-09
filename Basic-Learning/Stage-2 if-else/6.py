# Here's the Python code to determine if a character is a vowel or a consonant:

char = input("Enter a character: ")
if char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    print(char, "is a vowel")
else:
    print(char, "is a consonant")
