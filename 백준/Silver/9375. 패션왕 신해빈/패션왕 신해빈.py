import sys

tc = int(sys.stdin.readline().strip())

for _ in range(tc):
    n = int(sys.stdin.readline().strip())
    cls_dict = {}
    res = 1
    if n == 0:
        print(0)
    else:
        for _ in range(n):
            wear = sys.stdin.readline().strip().split()
            if wear[-1] not in cls_dict:
                cls_dict[wear[-1]] = 1
            else:
                cls_dict[wear[-1]] += 1
        # if len(cls_dict) == 1:
        #     print(n)
        # else:
        for i in cls_dict.values():
            res *= (i+1)
        print((res)-1)