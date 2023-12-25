import sys
def binary_search(num):
    start = 0
    end = num
    
    while start <= end:
        mid = (start + end)//2
        target = mid**2
        if target == num:
            print(mid)
            break

        elif target < num:
            start = mid+1
        else:
            end = mid-1
    
        

num = int(sys.stdin.readline().strip())
binary_search(num)
