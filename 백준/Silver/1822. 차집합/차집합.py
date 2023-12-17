import sys
n,m = map(int, sys.stdin.readline().strip().split())

list_a = set(list(map(int, sys.stdin.readline().strip().split())))
list_b = set(list(map(int, sys.stdin.readline().strip().split())))

res = list_a-list_b
res = list(res)
res.sort()


print(len(res))
if len(res) > 0:
    for i in res:
        print(i, end = ' ')