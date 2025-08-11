def matmul(A, B, mod):
    n = 2
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += A[i][k]*B[k][j]
            res[i][j] = s % mod
    return res

def matpow(A, n, mod):
    result = [[1, 0], [0, 1]]
    base = [row[:] for row in A]

    while n > 0:
        if n & 1:
            result = matmul(result, base, mod)
        base = matmul(base, base, mod)
        n >>= 1
    return result

def fib(n, mod=1000000):
    if n == 0:
        return 0
    A = [[1, 1],
         [1, 0]]
    An = matpow(A, n-1, mod)
    return An[0][0]

n = int(input())
print(fib(n))