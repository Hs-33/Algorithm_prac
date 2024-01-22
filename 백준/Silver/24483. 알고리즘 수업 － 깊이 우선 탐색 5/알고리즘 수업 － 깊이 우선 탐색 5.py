import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(graph, v, visited, depth):
    global cnt
    visited[v] = cnt*depth

    cnt += 1
    for i in sorted(graph[v]):
        if visited[i] == -1:
            # visited[v] = cnt* depth
            dfs(graph, i, visited, depth+1)
    return visited

n, m, r = map(int, input().strip().split())
cnt = 1
depth = 0
visited = [-1]*(n+1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

a = dfs(graph, r, visited, depth)
res = 0
for i in a[1:]:
    if i == -1:
        continue
    else:
        res += i
print(res)
