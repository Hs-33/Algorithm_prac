import sys
col_dict = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5,
        'blue':6, 'violet':7, 'grey':8, 'white':9}
arr = []
for _ in range(3):
    color = sys.stdin.readline().strip()
    arr.append(color)
result = int(str(col_dict[arr[0]])+str(col_dict[arr[1]]))*(10**col_dict[arr[2]])
print(result)