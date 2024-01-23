import sys
input = sys.stdin.readline
n, k = map(int, input().strip().split())
data = []

for _ in range(n):
    data.append(int(input().strip()))

data.sort()

def binary_search(data, target):
    start = 1
    end = data[-1]
    while start <= end:
        mid = (start+end)//2
        res = 0
        for i in data:
            res += (i//mid)
        if res >= target:
            start = mid + 1
        else:
            end = mid -1
    print(end)

binary_search(data, k)