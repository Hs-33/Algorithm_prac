import sys
text = sys.stdin.readline().strip()
lst = []
for i in range(len(text)):
    lst.append(text[i:])
lst.sort()
for i in lst:
    print(i)