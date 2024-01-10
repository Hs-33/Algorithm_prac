import sys

n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for i in range(n)]

arr.sort(reverse = True)

max = 0

for i in range(len(arr)):
    if i == 0:
        max = arr[i]
    else:
        if max < (arr[i])*(i+1):
            max = (arr[i])*(i+1)
print(max)


