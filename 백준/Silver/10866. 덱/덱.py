import sys
from collections import deque
n = int(sys.stdin.readline().strip())
num_deque = deque([])
for _ in range(n):
    arr = list(sys.stdin.readline().strip().split())

    if arr[0] == 'push_front':
        num_deque.appendleft(int(arr[1]))
    elif arr[0] == 'push_back':
        num_deque.append(int(arr[1]))
    elif arr[0] == 'pop_front':
        if len(num_deque) == 0:
            print(-1)
        else:
            print(num_deque.popleft())
    elif arr[0] == 'pop_back':
        if len(num_deque) == 0:
            print(-1)
        else:
            print(num_deque.pop())
    elif arr[0] == 'size':
        print(len(num_deque))
    elif arr[0] == 'empty':
        if len(num_deque) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 'front':
        if len(num_deque) == 0:
            print(-1)
        else:
            print(num_deque[0])
    elif arr[0] == 'back':
        if len(num_deque) == 0:
            print(-1)
        else:
            print(num_deque[-1])
