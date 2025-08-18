#include <stdio.h>
#include <stdint.h>

int main() {
    int64_t n, k;
    scanf("%lld %lld", &n, &k);

    int64_t r = 0;
    int64_t i = 1;

    while (i <= n) {
        int64_t q = k / i;
        int64_t next_i;
        if (q == 0) next_i = n;
        else next_i = k / q;

        if (next_i > n) next_i = n;

        int64_t cnt = next_i - i + 1;
        r += cnt * k;
        r -= q * cnt * (i + next_i) / 2;

        i = next_i + 1;
    }

    printf("%lld\n", r);
    return 0;
}
