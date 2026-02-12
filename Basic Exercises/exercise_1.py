# EXERCISE 1: STRINGS

# Write a program that prints:
# The total length of the string
# The first 5 characters
# The last 3 characters
# The string converted to lowercase
# How many times the substring "ATC" appears
# The string with all occurrences of "T" replaced by "U" (DNA to RNA transcription)


dna = "ATGCGATCGATCGATCGATCGA"

print("The DNA sequence is:", dna)
print("The total length is:", len(dna))
print("THe first 5 characters are:", dna[0:5])
print("The last 3 characters are:", dna[-3:])
print("Lowercase string:", dna.lower())
print("ATC count", dna.count("ATC"))
print("DNA to RNA transcription:", dna.replace("T", "U"))
