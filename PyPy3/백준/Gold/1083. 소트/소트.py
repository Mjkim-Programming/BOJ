def max_lex_with_swaps(arr, S):
    n = len(arr)
    arr = arr[:]
    for i in range(n):
        if S <= 0:
            break
        max_pos = i
        for j in range(i+1, min(n, i+S+1)):
            if arr[j] > arr[max_pos]:
                max_pos = j
        
        while max_pos > i and S > 0:
            arr[max_pos], arr[max_pos-1] = arr[max_pos-1], arr[max_pos]
            max_pos -= 1
            S -= 1
    
    return arr

N = int(input())
A = list(map(int, input().split()))
S = int(input())

res = max_lex_with_swaps(A, S)
print(*res)