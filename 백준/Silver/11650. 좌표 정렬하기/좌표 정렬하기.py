import sys
# from collections import deque
n = int(sys.stdin.readline().strip())
co_list = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    co_list.append((x, y))

co_list.sort()

for i in co_list:
    print(*i)