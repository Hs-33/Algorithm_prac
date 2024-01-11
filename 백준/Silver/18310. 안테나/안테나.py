import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()

if n%2 == 0:
    print(min(arr[(n//2)-1], arr[n//2]))
else:
    print(arr[n//2])