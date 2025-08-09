is_prime = [True] * (1000 + 1)
is_prime[0], is_prime[1] = False, False

for i in range(2, int(1000**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, 1000+1, i):
            is_prime[j] = False

n = int(input())
arr = list(map(int, input().split()))
c = 0

for i in arr:
    if is_prime[i]:
        c += 1

print(c)