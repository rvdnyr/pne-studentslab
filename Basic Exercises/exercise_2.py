# EXERCISE 2: MORE STRINGS

# Write a program that prints:
# The string with leading and trailing spaces removed (use strip())
# The number of words in the string (use split())
# The string with the first letter of each word capitalized (use title())
# Whether the stripped string starts with "Hello" (use startswith())
# Whether the stripped string ends with "ing." (use endswith())
# The position (index) of the word "Python" in the stripped string (use find())
# The words joined back together separated by " - " (use split() and " - ".join())


text = "  Hello, World! Welcome to Python Programming.  "

t_stripped = text.strip()
words_split = t_stripped.split(" ")

print("Stripped string:", t_stripped)
print("Word count:", len(t_stripped.split(" ")))
print("Title case:", t_stripped.title())
print("Starts with:", t_stripped.startswith("Hello"))
print("Ends with:", t_stripped.endswith("ing."))
print("Python position:", t_stripped.find("Python"))
print("Joined:", " - ".join(text.split())) # revisar esto
