# EXERCISE 5: LOOPS
# 5a: FOR loops

# Write a program that, given the list:

words = ["Python", "is", "a", "programming", "language"]

# Prints each word along with its length.


for i in range(0, len(words)):
    print(words[i] + " -> " + str(len(words[i])) + " characters")
