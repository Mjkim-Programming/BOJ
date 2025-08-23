import sys
sys.setrecursionlimit(10000)

a = input().strip()
b = input().strip()

cache = [[-1] * (len(b) + 1) for _ in range(len(a) + 1)]

def solve(aidx, bidx):
    if aidx == len(a) or bidx == len(b):
        return 0
    if cache[aidx][bidx] != -1:
        return cache[aidx][bidx]
    
    ret = solve(aidx + 1, bidx)
    ret = max(ret, solve(aidx, bidx + 1))
    ret = max(ret, solve(aidx + 1, bidx + 1) + (a[aidx] == b[bidx]))
    
    cache[aidx][bidx] = ret
    return ret

print(solve(0, 0))
