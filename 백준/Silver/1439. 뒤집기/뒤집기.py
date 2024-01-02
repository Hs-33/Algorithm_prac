import sys
str_ = sys.stdin.readline().strip()
# print(len(str_))
temp = []
for i in range(len(str_)-1):
    if len(temp) == 0:
        temp.append(int(str_[i]))
    if str_[i] != str_[i+1]:
        temp.append(int(str_[i+1]))
# test = list(map(int, temp))
if len(temp) == 0:
    print(0)
else:
    print(min(sum(temp), len(temp)-sum(temp)))