def fib(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fib(k-1) + fib(k-2)
import sys
n = int(sys.stdin.readline().strip())
res = fib(n)
print(res)