#include <stdio.h>

long long josephus_recursive(long long n, long long k) {
    if (n == 1) return 0;

    if (k > n)
        return (josephus_recursive(n - 1, k) + k) % n;

    long long res = josephus_recursive(n - n / k, k) - n % k;
    if (res < 0)
        return res + n;
    else
        return res + res / (k - 1);
}

long long josephus(long long n, long long k) {
    if (k == 1) return n;
    return josephus_recursive(n, k) + 1;
}

int main() {
    long long N, K;
    if (scanf("%lld %lld", &N, &K) != 2) return 1;

    printf("%lld\n", josephus(N, K));
    return 0;
}
