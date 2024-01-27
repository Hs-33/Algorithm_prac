from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(graph, node, visited):
    global cnt
    visited[node] = True
    # print(node)
            
    for i in sorted(graph[node]): 
        if not visited[i]: 
            cnt +=1
            dfs(graph, i, visited)
    

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n + 1)]
visited = [False]*(n+1)
cnt = 0

for _ in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1, visited)
print(cnt)

