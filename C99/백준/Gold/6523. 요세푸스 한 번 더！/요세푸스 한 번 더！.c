#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define HASH_SIZE 400003

typedef struct {
    int64_t key;
    int count;
} HashNode;

HashNode hash[HASH_SIZE];

int hash_insert(int64_t key) {
    int idx = key % HASH_SIZE;
    if (idx < 0) idx += HASH_SIZE;
    while (hash[idx].key != -1 && hash[idx].key != key) {
        idx = (idx + 1) % HASH_SIZE;
    }
    if (hash[idx].key == -1) {
        hash[idx].key = key;
        hash[idx].count = 1;
        return 1;
    } else {
        hash[idx].count++;
        return hash[idx].count;
    }
}

void hash_clear() {
    for (int i = 0; i < HASH_SIZE; i++) {
        hash[i].key = -1;
        hash[i].count = 0;
    }
}

int main() {
    int64_t N, a, b;

    while (scanf("%lld", &N) == 1 && N) {
        scanf("%lld %lld", &a, &b);

        hash_clear();
        int64_t x = 0;
        int stop = 0;

        while (1) {
            int cnt = hash_insert(x);
            if (cnt == 3) {
                break;
            }
            x = (a * x % N * x % N + b) % N;
        }

        int64_t total_home = N;
        for (int i = 0; i < HASH_SIZE; i++) {
            if (hash[i].key != -1 && hash[i].count >= 2) {
                total_home -= 1;
            }
        }

        printf("%lld\n", total_home);
    }

    return 0;
}
