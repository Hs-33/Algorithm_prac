import sys
n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
arr.sort(reverse = True)

for i in range(len(arr)-2):
    if arr[i] < arr[i+1]+arr[i+2]:
        print(arr[i]+arr[i+1]+arr[i+2])
        break
    if i == (len(arr)-3):
        print(-1)