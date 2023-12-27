import sys
n, m = map(int, sys.stdin.readline().strip().split())
lst = list(map(int, sys.stdin.readline().strip().split()))
lst.sort()
maximum = max(lst)

def binary_search(num, target):
    start = 1
    end = num
    while start <= end:
        mid = (start+end)//2
        length = 0
        for i in range(len(lst)):
            if lst[i] > mid:
                length += (lst[i]-mid)
        if length >= target:
            start = mid+1
        else:
            end = mid-1
    print(end)
binary_search(maximum, m)