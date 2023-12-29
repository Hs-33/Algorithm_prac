import sys
def binary_search(data, target):
    start = 0
    end = len(data)-1
    length = -1
    while start <= end:
        mid = (start + end)//2

        # if data[mid] == target:
        #     print(len(data[start:end+1]))
        
            
        if data[mid] < target:
            length = mid
            start = mid + 1
            
        elif data[mid] >= target:
            end = mid-1
    # print(len(data[:end+1]))
    return length 

tc = int(sys.stdin.readline().strip())

for _ in range(tc):
    n, m = map(int, sys.stdin.readline().strip().split())
    arr1 = list(map(int, sys.stdin.readline().strip().split()))
    arr2 = list(map(int, sys.stdin.readline().strip().split()))
    arr1.sort()
    arr2.sort()
    res = 0
    for i in range(len(arr1)):
        res += binary_search(arr2,arr1[i])+1
        
    print(res)