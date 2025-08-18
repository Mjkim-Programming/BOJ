#include <stdio.h>
#include <stdlib.h>

int tree[400000];
int n, k;

void build(int node, int start, int end) {
    if (start == end) {
        tree[node] = 1;
    } else {
        int mid = (start + end) / 2;
        build(node*2, start, mid);
        build(node*2+1, mid+1, end);
        tree[node] = tree[node*2] + tree[node*2+1];
    }
}

int query(int node, int start, int end, int k) {
    tree[node]--;
    if (start == end) {
        return start;
    }
    int mid = (start + end) / 2;
    if (tree[node*2] >= k) {
        return query(node*2, start, mid, k);
    } else {
        return query(node*2+1, mid+1, end, k - tree[node*2]);
    }
}

int main() {
    scanf("%d %d", &n, &k);
    build(1, 1, n);

    int idx = k;
    printf("<");
    for (int i = 0; i < n; i++) {
        int remain = n - i;
        if (idx > remain) {
            idx = idx % remain;
            if (idx == 0) idx = remain;
        }
        int person = query(1, 1, n, idx);
        printf("%d", person);
        if (i != n-1) printf(", ");
        idx += k - 1;
    }
    printf(">\n");
    return 0;
}
