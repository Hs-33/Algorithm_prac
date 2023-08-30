import sys
n = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

nums.sort()

def mode(num_list):
    freq_dict = {}
    for i in num_list:
        if i not in freq_dict:
            freq_dict[i] = 1
        else:
            freq_dict[i] += 1
    sorted_dict = {k: v for k, v in sorted(freq_dict.items(), key=lambda item: item[1])}
    return sorted_dict

freq_dict = mode(nums)

temp = []
for key, val in freq_dict.items():
    if val == max(freq_dict.values()):
        temp.append([key])
temp.sort()
if len(temp) == 1:
    mode = temp[0]
else:
    mode = temp[1]

mean = round(sum(nums)/len(nums))
median = nums[len(nums)//2]
range = max(nums)-min(nums)

print(mean)
print(median)
print(*mode)
print(range)