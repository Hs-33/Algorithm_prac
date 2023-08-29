import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        arr.append(command[-1])
    elif command[0] == 'pop':
        if len(arr) != 0:
            print(arr.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(arr))
    elif command[0] == 'empty':
        if len(arr) != 0:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if len(arr) != 0:
            print(arr[-1])
        else:
            print(-1)