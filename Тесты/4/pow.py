import math as m

def pow2(a):
    return a * a

def pow2_math(a):
    return m.pow(a, 2)

def pow3_math(a):
    return m.pow(a, 3)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b