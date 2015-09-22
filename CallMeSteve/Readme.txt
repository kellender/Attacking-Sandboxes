This works:
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)

print fib(1.0) 


Seg fault by means of negative number in fib function. 
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)

print fib(-1) 
Unauthorized memory access made by the function that goes in an infinite loop
