
#fibonacci numbers from 1-10.
def fib(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:

        return fib(x-1)+ fib(x-2)

for x in range (0,10):
    print fib(x)
