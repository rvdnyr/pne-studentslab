# EXERCISE 4: CONDITIONALS

# Write a program that, given a variable score containing a numeric grade between 0 and 10, prints the corresponding
# letter grade according to this table:
# Score - Letter
# 9.0 - 10.0 - A
# 7.0 - 8.9 - B
# 5.0 - 6.9 - C
# 3.0 - 4.9 - D
# 0.0 - 2.9 - F
# Test your program with the following values: 9.5, 7.0, 5.5, 3.2, 1.0


def score_letter(score):
    if 9 <= score <= 10:
        return "Score " + str(score) + " --> A" # como devuelve un string, hay que transformar el número a str, y para unirlos se pone el +
    elif 7 <= score <= 8.9:
        return "Score " + str(score) + " --> B"
    elif 5 <= score <= 6.9:
        return "Score " + str(score) + " --> C"
    elif 3 <= score <= 4.9:
        return "Score " + str(score) + " --> D"
    elif 0 <= score <= 2.9:
        return "Score " + str(score) + " --> F"

print(score_letter(9.5))
print(score_letter(7.0))
print(score_letter(5.5))
print(score_letter(3.2))
print(score_letter(1.0))
