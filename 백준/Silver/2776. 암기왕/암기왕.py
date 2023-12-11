import sys

def binary_search(target, data):
    cnt = 0
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
tc = int(sys.stdin.readline().strip())

for _ in range(tc):
    n = int(sys.stdin.readline().strip())
    num_list1 = list(map(int,sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    num_list2 = list(map(int,sys.stdin.readline().strip().split()))

    num_list1.sort()
    num_list1_t = num_list1

    for i in range(len(num_list2)):
        if binary_search(num_list2[i], num_list1):
            print(1, end = ' ')
        else:
            print(0, end = ' ')