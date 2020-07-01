def fib(x):
    if x == 1: return 1
    if x == 0: return 0
    return fib(x-1) + fib(x-2)
