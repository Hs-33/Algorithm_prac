import sys

N, M = map(int, sys.stdin.readline().strip().split())

lst_a = [int(sys.stdin.readline().strip()) for _ in range(N)]
lst_b = [int(sys.stdin.readline().strip()) for _ in range(M)]

lst_a.sort()

for i in range(M):
    start = 0
    end = len(lst_a)-1
    while start <= end:
        mid = (start + end) // 2
        if lst_a[mid] == lst_b[i]:
            if end == mid:
                break
            end = mid

            
        elif lst_a[mid] > lst_b[i]:
            end = mid-1
        else:
            start = mid+1
    if lst_a[mid] == lst_b[i]:
        print(mid)
    else:
        print(-1)