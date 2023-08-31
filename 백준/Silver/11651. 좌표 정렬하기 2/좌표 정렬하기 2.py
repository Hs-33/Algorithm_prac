import sys
# from collections import deque
n = int(sys.stdin.readline().strip())
co_list = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    co_list.append((y, x))

co_list.sort()

for i in co_list:
    y, x = i
    print(x, y)