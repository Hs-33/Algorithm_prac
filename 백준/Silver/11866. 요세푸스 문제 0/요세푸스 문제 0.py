import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
que = deque(i+1 for i in range(N))
arr = []
while N!=0:
    for _ in range(K-1):
        que.append(que.popleft())
    arr.append(str(que.popleft()))
    N-=1
print('<',', '.join(arr),'>', sep='')