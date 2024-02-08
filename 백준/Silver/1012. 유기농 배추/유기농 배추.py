import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(row,col):
    drow = [-1,1,0,0]
    dcol = [0,0,-1,1]
    
    for fi in range(4):
        nrow = row + drow[fi]
        ncol = col + dcol[fi]
        # print(nrow, ncol)
        if (nrow >= 0) and (nrow <= (m-1)) and (ncol >= 0) and (ncol <= (n-1)):
            if graph[nrow][ncol] == 1:
                graph[nrow][ncol] = 0
                dfs(nrow, ncol)

    


tc = int(input().strip())
for _ in range(tc):
    n, m, k = map(int, input().strip().split())
    graph = [[0]*(n) for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().strip().split())
        graph[b][a] = 1

    cnt = 0
    for r in range(m):
        for c in range(n):
            if graph[r][c] == 1:
                dfs(r, c)
                cnt += 1

    print(cnt)

