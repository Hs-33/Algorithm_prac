import sys
n, m = map(int, sys.stdin.readline().strip().split())

def factorial(num):
    res = 1
    for i in range(1,num+1):
        res *= i
    return res
print(factorial(n)//(factorial(n-m)*factorial(m)))