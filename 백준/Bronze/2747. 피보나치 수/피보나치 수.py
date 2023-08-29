import sys
N = int(sys.stdin.readline().strip())
arr = [1,1]
i = 3
if N == 0:
    print(0)
if N == 1 or N ==2:
    print(1)
while i <= N:
    res = arr[0] + arr[1]
    if i == N:
        print(res)
        break
    arr[0] = arr[1]
    arr[1] = res

    i += 1