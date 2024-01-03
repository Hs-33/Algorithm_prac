import sys    
    
def binary_search(data, target):
    start = 0
    end = len(data)-1
    temp = 0
    asw = []
    while start <= end:
        mid = (start+end)//2
        if data[mid] >= target:
            asw.append(data[mid]-target)
            end = mid -1

        elif data[mid] < target:
            start = mid + 1
    return asw

tc, m = map(int,sys.stdin.readline().strip().split())
res = []

for _ in range(tc):
    arrival, step, num = map(int, sys.stdin.readline().strip().split())
    data = [arrival+(step*(i)) for i in range(num)]
    data.sort()
    asw_lst = binary_search(data, m)
    if asw_lst:
        res.append(min(asw_lst))
    

print(min(res) if res else -1)
