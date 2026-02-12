# EXERCISE 6: FUNCTIONS
# 6b: function with multiple parameters

# Write a function called classify_triangle(a, b, c) that receives the lengths of the three sides
# of a triangle and returns:
# "equilateral" if all three sides are equal
# "isosceles" if exactly two sides are equal
# "scalene" if all three sides are different
# Test it with: (5, 5, 5), (3, 3, 4), (3, 4, 5)


def classify_triangle(a, b, c):
    if a == b == c:
        return "triangle of length sides: " + str(a) + " " + str(b) + " " + str(c) + " -> equilateral"
    elif a == b or b == c or a == c:
        return "triangle of length sides: " + str(a) + " " + str(b) + " " + str(c) + " -> isosceles"
    else:
        return "triangle of length sides: " + str(a) + " " + str(b) + " " + str(c) + " -> scalene"

print(classify_triangle(5,5,5))
print(classify_triangle(3,3,4))
print(classify_triangle(3,4,5))
