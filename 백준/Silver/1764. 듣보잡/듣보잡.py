import sys
n, m = map(int, sys.stdin.readline().strip().split())
n_h = []
n_s = []
for i in range(n+m):
    name = sys.stdin.readline().strip()
    if i < n:
        n_h.append(name)
    else:
        n_s.append(name)
res = set(n_h) & set(n_s)
res = sorted(list(res))

print(len(res))
for i in res:
    print(i)