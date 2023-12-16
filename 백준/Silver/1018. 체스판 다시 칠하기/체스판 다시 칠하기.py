import sys
n, m = map(int, sys.stdin.readline().strip().split())

arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

def count(n,m,arr):
    cnt_w = 0
    cnt_b = 0
    for i in range(1, len(arr)+1):
        for j in range(1, len(arr)+1):
            
            if (i%2 != 0) and (j%2 != 0):
                if arr[i-1][j-1] != 'W':
                    cnt_w += 1
            elif (i%2 != 0) and (j%2 == 0):
                if arr[i-1][j-1] != 'B':
                    cnt_w += 1
            elif (i%2 == 0) and (j%2 != 0):
                if arr[i-1][j-1] != 'B':
                    cnt_w += 1
            elif (i%2 == 0) and (j%2 == 0):
                if arr[i-1][j-1] != 'W':
                    cnt_w += 1

    for i in range(1, len(arr)+1):
        for j in range(1, len(arr)+1):
            if (i%2 != 0) and (j%2 != 0):
                if arr[i-1][j-1] != 'B':
                    cnt_b += 1
            elif (i%2 != 0) and (j%2 == 0):
                if arr[i-1][j-1] != 'W':
                    cnt_b += 1
            elif (i%2 == 0) and (j%2 != 0):
                if arr[i-1][j-1] != 'W':
                    cnt_b += 1
            elif (i%2 == 0) and (j%2 == 0):
                if arr[i-1][j-1] != 'B':
                    cnt_b += 1

    return min(cnt_w, cnt_b)

save = []
for i in range(n-7):
    for j in range(m-7):
        arr_part = [a[j:j + 8]for a in arr[i:i + 8]]
        min_ = count(m, n, arr_part)
        save.append(min_)

print(min(save))