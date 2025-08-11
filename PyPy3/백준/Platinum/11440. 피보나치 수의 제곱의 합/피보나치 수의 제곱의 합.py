MOD = 10**9 + 7

def matmul(A, B):
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]]

def matpow(M, n):
    result = [[1, 0], [0, 1]]
    base = M
    while n > 0:
        if n & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        n >>= 1
    return result

def fib(n):
    if n == 0:
        return 0
    M = [[1,1],[1,0]]
    Mn = matpow(M, n-1)
    return Mn[0][0]

n = int(input())
Fn = fib(n)
Fn1 = fib(n+1)
answer = (Fn * Fn1) % MOD
print(answer)