# EXERCISE 6: FUNCTIONS
# 6a: basic function

# Write a function called is_even(number) that returns True if the number is even and False otherwise.
# Test it with the numbers: 4, 7, 0, -3, 10


def is_even(number):
    return "Number " + str(number) + " -> " + str(number % 2 == 0)

print("Even numbers?")
print(is_even(4))
print(is_even(7))
print(is_even(0))
print(is_even(-3))
print(is_even(10))
