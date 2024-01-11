import sys
from collections import deque
def count_let(str):
    arr = []
    temp = 1
    for i in range(len(str)-1):
        if str[i] == str[i+1] :
            temp += 1
        elif str[i] != str[i+1]:
            if temp%2 != 0:
                arr.append(1)
            else:
                arr.append(0)
            temp = 1
        if i == (len(str)-2):
            if temp%2 != 0:
                arr.append(1)
            else:
                arr.append(0)
            temp = 1
            
    return sum(arr)

text = list(sys.stdin.readline().strip())
text.sort()
text = deque(text)

an = count_let(text)
arr = [0]*len(text)

if an > 1:
    print("I'm Sorry Hansoo")
elif len(text) == 1:
    print(*text)
else:
    i = 0
    while True:
        if text[0] == text[1]:
            arr[i] = text.popleft()
            arr[-i-1] = text.popleft()
            i += 1
        else:
            text.append(text.popleft())
            continue
        if len(text) == 1:
            arr[(len(arr)//2)] = text.popleft()
            print(''.join(arr))
            break
        elif len(text) == 0:
            print(''.join(arr))
            break
        