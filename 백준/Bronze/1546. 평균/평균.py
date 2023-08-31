import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int,sys.stdin.readline().strip().split()))
summation = 0
for i in nums:
    res = (i/max(nums))*100
    summation += res
print(summation/len(nums))