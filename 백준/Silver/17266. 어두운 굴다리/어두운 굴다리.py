import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

maxi = 0
for i in range(len(arr)-1):
    if (abs(arr[i]-arr[i+1]))/2 > maxi:
        maxi = ((abs(arr[i]-arr[i+1]))/2)
if maxi-int(maxi) > 0:
    maxi = int(maxi)+1
print(max(int(maxi),abs(0-arr[0]), abs(arr[-1]-n)))