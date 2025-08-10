from collections import deque

dfs_visited = []

def dfs(graph, v, visited):
    visited[v] = True
    dfs_visited.append(v)
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    res = []
    while queue:
        v = queue.popleft()
        res.append(v)
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return res

n, m, start = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
dfs(graph, start, visited)
print(*dfs_visited)

visited = [False] * (n+1)
print(*bfs(graph, start, visited))