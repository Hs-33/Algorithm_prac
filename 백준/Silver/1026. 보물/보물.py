import sys

n = int(sys.stdin.readline().strip())
lst_a = list(map(int, sys.stdin.readline().strip().split()))
lst_b = list(map(int, sys.stdin.readline().strip().split()))

lst_a.sort()
lst_b.sort()

res = 0
for i in range(n):
    res += (lst_a[i]*lst_b[n-i-1])
print(res)