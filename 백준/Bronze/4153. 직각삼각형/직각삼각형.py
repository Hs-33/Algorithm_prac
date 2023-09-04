import sys
while True:
    lens = list(map(int, sys.stdin.readline().strip().split()))
    lens.sort()
    if sum(lens) == 0:
        break
    len_1 = (lens[0]**2) + (lens[1]**2)
    if len_1 == lens[-1]**2:
        print('right')
    else:
        print('wrong')