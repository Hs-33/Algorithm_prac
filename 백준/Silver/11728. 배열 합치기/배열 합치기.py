N, M = map(int,input().split())
res = []
for _ in range(2):
    n= [int(i) for i in input().split()]
    res = res+n

res.sort()

print(*res)