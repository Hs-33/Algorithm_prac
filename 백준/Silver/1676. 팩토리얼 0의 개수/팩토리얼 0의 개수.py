import sys
N = int(sys.stdin.readline().strip())
res = 1
if N == 0:
    res = 1
else:
    for i in range(1,N+1):
        res *= i
cnt = 0
for i in reversed(str(res)):
    if i != '0':
        break
    else:
        cnt += 1
print(cnt)