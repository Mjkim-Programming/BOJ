def check_no_k_repetition(s, K):
    length = len(s)
    for l in range(1, length // K + 1):
        pattern = s[-l:]
        repeated = pattern * K
        if length >= l * K and s[-l*K:] == repeated:
            return False
    return True

def solve(K, N, A):
    alphabet = [chr(ord('A') + i) for i in range(A)]
    result = []

    def backtrack(pos):
        if pos == N:
            return True
        for c in alphabet:
            result.append(c)
            if check_no_k_repetition(result, K):
                if backtrack(pos + 1):
                    return True
            result.pop()
        return False

    backtrack(0)
    if result == '':
        return '-1'
    if not result:
        return '-1'
    return ''.join(result)

K, N, A = map(int, input().split())
print(solve(K, N, A))