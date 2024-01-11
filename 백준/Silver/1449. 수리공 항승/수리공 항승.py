import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

arr.sort()

temp = 0
cnt = 1

for i in range(len(arr)-1):
    if temp + abs(arr[i]-arr[i+1]) < m:
        temp += abs(arr[i]-arr[i+1])
    else:
        cnt += 1
        temp = 0
print(cnt)