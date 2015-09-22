def fibonacci(fibNum):
    a,b = 1,1
    for i in range(fibNum-1):
        a,b = b,a+b
    print a

fibonacci(10)


