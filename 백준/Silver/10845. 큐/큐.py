from collections import deque
import sys
N = int(sys.stdin.readline())
que = deque()

for _ in range(N):
    arr = sys.stdin.readline().split()

    if arr[0] == 'push':
        que.append(arr[1])
    elif arr[0] == 'pop':
        if len(que) != 0:
            print(que.popleft())
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(que))
    elif arr[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 'front':
        if len(que) != 0:
            print(que[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)