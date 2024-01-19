import sys

def dfs(start, graph, n):
    stack = [start]
    visit = set()
    res = [0] * (n + 1)
    cnt = 1

    while stack:
        curr = stack.pop()

        if curr not in visit:
            res[curr] = cnt
            cnt += 1
            visit.add(curr)

        for nxt in sorted(graph[curr]):
            if nxt not in visit:
                stack.append(nxt)

    return res[1:]

n, m, r = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# No need to sort each adjacency list, as we're sorting during traversal
result = dfs(r, graph, n)

for a in result:
    print(a)
