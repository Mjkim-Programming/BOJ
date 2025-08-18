#include <stdio.h>

long long josephus(long long n, long long k) {
    long long res = 0;
    for (long long i = 2; i <= n; i++) {
        res = (res + k) % i;
    }
    return res + 1;
}

int main() {
    long long N, K;
    if (scanf("%lld %lld", &N, &K) != 2) return 1;
    printf("%lld\n", josephus(N, K));
    return 0;
}
