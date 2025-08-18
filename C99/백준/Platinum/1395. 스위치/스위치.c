#include <stdio.h>
#include <stdlib.h>

#define MAXN 100000

typedef struct {
    int sum;
    int lazy;
} Node;

Node tree[4*MAXN];
int N, M;

void push(int node, int l, int r) {
    if (tree[node].lazy) {
        tree[node].sum = (r - l + 1) - tree[node].sum;
        if (l != r) {
            tree[node*2].lazy ^= 1;
            tree[node*2+1].lazy ^= 1;
        }
        tree[node].lazy = 0;
    }
}

void update(int node, int l, int r, int ql, int qr) {
    push(node, l, r);
    if (r < ql || l > qr) return;
    if (ql <= l && r <= qr) {
        tree[node].lazy ^= 1;
        push(node, l, r);
        return;
    }
    int m = (l + r) / 2;
    update(node*2, l, m, ql, qr);
    update(node*2+1, m+1, r, ql, qr);
    tree[node].sum = tree[node*2].sum + tree[node*2+1].sum;
}

int query(int node, int l, int r, int ql, int qr) {
    push(node, l, r);
    if (r < ql || l > qr) return 0;
    if (ql <= l && r <= qr) return tree[node].sum;
    int m = (l + r) / 2;
    return query(node*2, l, m, ql, qr) + query(node*2+1, m+1, r, ql, qr);
}

int main() {
    scanf("%d %d", &N, &M);
    for (int i=0; i<M; i++) {
        int O, S, T;
        scanf("%d %d %d", &O, &S, &T);
        if (O == 0) {
            update(1, 1, N, S, T);
        } else {
            printf("%d\n", query(1, 1, N, S, T));
        }
    }
    return 0;
}
