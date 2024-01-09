import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().strip().split()))
res = 0
temp = 0
arr.sort()
for i in arr:
    temp += i
    res += temp
print(res)