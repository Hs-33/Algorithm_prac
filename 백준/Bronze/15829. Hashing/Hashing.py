import sys
input = sys.stdin.readline
n = int(input().strip())
text = input().strip()
res = 0
for i in range(len(text)):
    res += (ord(text[i])-96)*(31**i)
print(res)