# Write a function called fibosum(n) that calculates the addition of the n first fibonacci terms.
# The main program should call this function twice, with the arguments n=5 and n=10.


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

def fibosum(n):
    fibo_numbers = []
    for w in range(0,n):
        fibo_numbers.append(fibon(w))
        #print("The first", (w + 1), "numbers of the Fibonacci series are:", fibo_numbers) # just to check if it is running correctly :P
    return sum(fibo_numbers)

print("The sum of the first 5 terms of the Fibonacci series is:", fibosum(5))
print("The sum of the first 10 terms of the Fibonacci series is:", fibosum(10))
