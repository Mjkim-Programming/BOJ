import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

LOG = 17
parent = [[-1]*(LOG+1) for _ in range(N+1)]
depth = [0]*(N+1)
dist_from_root = [0]*(N+1)

def dfs(u, p):
    for v, w in graph[u]:
        if v != p:
            depth[v] = depth[u]+1
            dist_from_root[v] = dist_from_root[u]+w
            parent[v][0] = u
            dfs(v,u)

dfs(1,-1)

for k in range(1, LOG+1):
    for v in range(1, N+1):
        if parent[v][k-1] != -1:
            parent[v][k] = parent[parent[v][k-1]][k-1]

def lca(u,v):
    if depth[u] < depth[v]:
        u,v = v,u
    for k in range(LOG,-1,-1):
        if parent[u][k] != -1 and depth[parent[u][k]] >= depth[v]:
            u = parent[u][k]
    if u == v:
        return u
    for k in range(LOG,-1,-1):
        if parent[u][k] != -1 and parent[u][k] != parent[v][k]:
            u = parent[u][k]
            v = parent[v][k]
    return parent[u][0]

def kth_node(u,v,k):
    anc = lca(u,v)
    du = depth[u]-depth[anc]+1
    dv = depth[v]-depth[anc]
    if k <= du:
        node = u
        k -= 1
        for i in range(LOG,-1,-1):
            if k >= (1<<i):
                node = parent[node][i]
                k -= (1<<i)
        return node
    else:
        k = k - du
        node = v
        steps = dv - k
        for i in range(LOG,-1,-1):
            if steps >= (1<<i):
                node = parent[node][i]
                steps -= (1<<i)
        return node

M = int(input())
for _ in range(M):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        u,v = tmp[1], tmp[2]
        anc = lca(u,v)
        print(dist_from_root[u]+dist_from_root[v]-2*dist_from_root[anc])
    else:
        u,v,k = tmp[1], tmp[2], tmp[3]
        print(kth_node(u,v,k))
