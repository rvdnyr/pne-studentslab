# Write a program (without creating any function) that prints on the console the first 11 terms of the Fibonacci series (starting from 0).


print("The first 11 terms of the Fibonacci series are:")

for n in range(0,11):
    a = 0
    b = 1
    if n == a:
        print(a)
    elif n == b:
        print(b)
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        print(c)
