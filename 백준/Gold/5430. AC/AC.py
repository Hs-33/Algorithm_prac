from collections import deque
import sys
input = sys.stdin.readline

tc = int(input().strip())
for _ in range(tc):
    func = list(input().strip())
    length= int(input().strip())
    temp = input().strip()
    if length == 0:
        data = deque()
    else:
        data = deque(temp[1:-1].split(','))
    # print(data)
    # print(len(data))

    
    rev = 0

    for i in func:
        stat = True
        
            
        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(data)==0:
                print('error')
                stat = False
                break
            else:
                if rev%2 == 1:
                    data.pop()
                else:
                    data.popleft()

       
    if stat:
        if rev%2 == 1:
            data.reverse()
            print("[" + ",".join(data) + "]")  
        else:
            print("[" + ",".join(data) + "]")
