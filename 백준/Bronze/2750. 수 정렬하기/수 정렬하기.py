import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

left = []
right = []

num = [arr[-1]]
for i in range(len(arr)-1):
    if arr[i] < num[0]:
        left.append(arr[i])
        for j in range(len(left)-1):
            if left[j] > left[-1]:
                left[j], left[-1] = left[-1], left[j]
            else:
                continue

    if arr[i] > num[0]:
        right.append(arr[i])
        for j in range(len(right)-1):
            if right[j] > right[-1]:
                right[j], right[-1] = right[-1], right[j]
            else:
                continue

s_arr = left+num+right

for s in s_arr:
    print(s)