import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        self.N = len(data)
        self.size = 1
        while self.size < self.N:
            self.size *= 2
        self.tree = [(float('inf'), -1)] * (2*self.size)
        for i, val in enumerate(data):
            self.tree[self.size + i] = (val, i+1)
        for i in range(self.size-1, 0, -1):
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])
    
    def update(self, pos, value):
        pos = self.size + pos - 1
        self.tree[pos] = (value, pos - self.size + 1)
        while pos > 1:
            pos //= 2
            self.tree[pos] = min(self.tree[2*pos], self.tree[2*pos+1])
    
    def query(self):
        return self.tree[1][1]

N = int(input())
arr = list(map(int, input().split()))
st = SegmentTree(arr)

M = int(input())
for _ in range(M):
    q = list(map(int, input().split()))
    if q[0] == 2:
        print(st.query())
    else:
        st.update(q[1], q[2])
