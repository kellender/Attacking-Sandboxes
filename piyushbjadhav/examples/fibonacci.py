a, b = 1, 1
print a
for i in range(9):
    a, b = b, a + b
    print a
