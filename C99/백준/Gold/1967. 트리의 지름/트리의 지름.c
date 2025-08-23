#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_NODES 100001

struct Edge {
    int to, weight;
    struct Edge* next;
};

typedef struct Edge Edge;

Edge* adj[MAX_NODES];
int visited[MAX_NODES];
int max_dist = 0, farthest_node = 0;

void add_edge(int from, int to, int weight) {
    Edge* edge = (Edge*)malloc(sizeof(Edge));
    edge->to = to;
    edge->weight = weight;
    edge->next = adj[from];
    adj[from] = edge;
}

void dfs(int node, int dist) {
    visited[node] = 1;
    if (dist > max_dist) {
        max_dist = dist;
        farthest_node = node;
    }
    for (Edge* edge = adj[node]; edge != NULL; edge = edge->next) {
        if (!visited[edge->to]) {
            dfs(edge->to, dist + edge->weight);
        }
    }
}

int main() {
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N - 1; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        add_edge(u, v, w);
        add_edge(v, u, w);
    }

    memset(visited, 0, sizeof(visited));
    dfs(1, 0);

    memset(visited, 0, sizeof(visited));
    max_dist = 0;
    dfs(farthest_node, 0);

    printf("%d\n", max_dist);

    return 0;
}
