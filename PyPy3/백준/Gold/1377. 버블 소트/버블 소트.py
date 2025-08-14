N = int(input())
A = [int(input()) for _ in range(N)]

B = sorted(A)
pos = {v: i for i, v in enumerate(B)}

max_shift = 0
for i in range(N):
    shift = i - pos[A[i]]
    if shift > max_shift:
        max_shift = shift

print(max_shift + 1)
