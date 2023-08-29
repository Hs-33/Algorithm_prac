i = 1
result = 0
arr = []

while True:
    nums = list(map(int, list(str(i))))
    result = i+sum(nums)
    if i > 10000:
        break
    arr.append(result)
    result = 0
    i +=1

arr = set(arr)
#
for i in range(10000):
    if i+1 not in arr:
        print(i+1)
