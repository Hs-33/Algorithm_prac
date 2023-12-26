import sys
from collections import deque
n, k = map(int, input().split())
lst = deque([i for i in range(1,n+1)])

arr = []
while n!=0:
    for _ in range(k-1):
        lst.append(lst.popleft())
    arr.append(str(lst.popleft()))
    n-=1
print('<',', '.join(arr),'>', sep='')