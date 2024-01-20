import sys
a, b, v = map(int, sys.stdin.readline().strip().split())
res = (v-b)/(a-b)
if int(res)-res < 0:
    print(int(res)+1)
else:
    print(int(res))