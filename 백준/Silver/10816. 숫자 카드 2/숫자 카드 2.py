import sys
n = int(sys.stdin.readline().strip())
num_list1 = list(map(int,sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
num_list2 = list(map(int,sys.stdin.readline().strip().split()))

num_list1.sort()

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True 
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return False

d = {}
for i in num_list1:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for i in range(len(num_list2)):
    if binary_search(num_list2[i], num_list1):
        print(d[num_list2[i]], end = ' ')
    else:
        print(0, end = ' ')
