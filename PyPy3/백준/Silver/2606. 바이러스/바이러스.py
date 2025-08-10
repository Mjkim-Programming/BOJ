from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
queue = deque([1])
visited[1] = True
count = 0

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)
            count += 1

print(count)