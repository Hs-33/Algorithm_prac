from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, node, visited):
    global res
    cnt = 1
    que = deque([node])
    visited[node] = True
    res[node] = cnt
    while que:
        node = que.popleft()
        # print(node)
                
        for i in sorted(graph[node]):
            if not visited[i]:
                cnt += 1
                que.append(i)
                visited[i] = True
                res[i] = cnt

n, m, r = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
res = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)


bfs(graph, r, visited)

for i in res[1:]:
    print(i)
