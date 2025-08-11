def matmul_inplace(A, B, n, mod=None):
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += A[i][k] * B[k][j]
            tmp[i][j] = s % mod if mod else s
    return tmp

def matpow_optimized(A, exp, mod=None):
    n = len(A)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    base = [row[:] for row in A]
    while exp:
        if exp & 1:
            result = matmul_inplace(result, base, n, mod)
        base = matmul_inplace(base, base, n, mod)
        exp >>= 1
    return result

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = matpow_optimized(arr, b, 1000)

for row in res:
    print(*row)