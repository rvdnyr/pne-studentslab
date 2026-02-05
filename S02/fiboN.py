# Convert the previous program into the function fibon(n) that calculates the nth Fibonacci term and return it.
# The main program should call the fibon() function and print the 5th, 10th and 15th terms in the console.


def fibon(n):
    a = 0
    b = 1
    if n == a:
        return a
    elif n == b:
        return b
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return c

print("The 5th term of the Fibonacci series is:", fibon(5))
print("The 10th term of the Fibonacci series is:", fibon(10))
print("The 15th term of the Fibonacci series is:", fibon(15))
