FIB = {"max": 1, 0: 0, 1: 1}

#Fibonacci sequence calulated non-recusively and much faster than a, b = 0, 1 method

def fibonacci(n):
    for i in range(FIB["max"] + 1, n + 1):
        FIB[i] = FIB[i - 1] + FIB[i - 2]
        FIB["max"] = i

    return FIB[n]
