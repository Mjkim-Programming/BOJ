import math

N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())

total_bundles = (
    math.ceil(S / T) +
    math.ceil(M / T) +
    math.ceil(L / T) +
    math.ceil(XL / T) +
    math.ceil(XXL / T) +
    math.ceil(XXXL / T)
)

pen_bundle = N // P
pen_single = N % P

print(total_bundles)
print(pen_bundle, pen_single)