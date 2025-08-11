MOD = 1000000007

def mat_mul(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def mat_pow(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        half = mat_pow(A, n // 2)
        return mat_mul(half, half)
    else:
        half = mat_pow(A, (n - 1) // 2)
        return mat_mul(mat_mul(half, half), A)

n = int(input())
if n == 0:
    print(0)
else:
    base = [[1, 1], [1, 0]]
    result = mat_pow(base, n)
    print(result[0][1])