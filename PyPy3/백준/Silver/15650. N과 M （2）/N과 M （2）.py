from itertools import combinations

N, M = map(int, input().split())
if M < 3 :
    ansc = list(combinations(range(1,N+1), M))
    for x in ansc :
        print(*x)
else :
    ansc = list(combinations(range(1,N+1), M))
    for x in ansc :
        print(*x)