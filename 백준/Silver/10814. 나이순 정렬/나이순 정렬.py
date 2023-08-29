import sys

n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    age, name = sys.stdin.readline().strip().split()
    age = int(age)

    arr.append([age, name])
arr.sort(key = lambda x: x[0])
for i in arr:
    print(*i)
