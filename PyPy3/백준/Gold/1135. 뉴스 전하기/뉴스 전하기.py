N = int(input())
boss = list(map(int, input().split()))

children = [[] for _ in range(N)]
for i in range(1, N):
    children[boss[i]].append(i)

def dfs(node):
    if not children[node]:
        return 0

    times = []
    for child in children[node]:
        times.append(dfs(child))

    times.sort(reverse=True)

    max_time = 0
    for i in range(len(times)):
        max_time = max(max_time, times[i] + i + 1)

    return max_time

print(dfs(0))