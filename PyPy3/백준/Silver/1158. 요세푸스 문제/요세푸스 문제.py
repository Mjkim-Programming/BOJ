from collections import deque

def josephus(n, k):
    res = []
    q = deque(range(1, n + 1))
    while q:
        q.rotate(-(k - 1))
        res.append(q.popleft())
    return res

n, k = map(int, input().split())
res = josephus(n, k)
print("<" + ", ".join(map(str, res)) + ">")