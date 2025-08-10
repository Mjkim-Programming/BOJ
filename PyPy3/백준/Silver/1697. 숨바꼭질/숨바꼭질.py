from collections import deque

N, K = map(int, input().split())
MAX = 100000
visited = [-1] * (MAX + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = 0

    while queue:
        x = queue.popleft()
        if x == K:
            return visited[x]

        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

print(bfs(N))