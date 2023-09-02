import sys

while True:
    num = sys.stdin.readline().strip()
    if int(num) == 0:
        break
    cnt = 0
    for i in range(len(num)//2):
        if num[i] == num[-(i+1)]:
            cnt += 1
        else:
            continue
    if cnt == len(num)//2:
        print('yes')
    else:
        print('no')