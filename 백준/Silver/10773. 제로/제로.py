import sys
N = int(sys.stdin.readline())
number = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        number.append(num)
    else:
        del number[-1]
print(sum(number))