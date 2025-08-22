#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXN 100005

typedef struct {
    int to, idx, next;
} Edge;

Edge edges[MAXN*2];
int head[MAXN], edge_cnt;
int parent[MAXN], depth[MAXN], heavy[MAXN], size[MAXN];
int top[MAXN], pos[MAXN], edge_to_node[MAXN];
int seg[4*MAXN];
int cur_pos;

void add_edge(int u, int v, int idx){
    edges[edge_cnt].to = v;
    edges[edge_cnt].idx = idx;
    edges[edge_cnt].next = head[u];
    head[u] = edge_cnt++;
}

int max(int a, int b){ return a>b?a:b; }

int dfs(int u){
    size[u]=1;
    int max_size=0;
    for(int i=head[u]; i!=-1; i=edges[i].next){
        int v = edges[i].to;
        if(v==parent[u]) continue;
        parent[v]=u;
        depth[v]=depth[u]+1;
        int sz=dfs(v);
        size[u]+=sz;
        if(sz>max_size){
            max_size=sz;
            heavy[u]=v;
        }
    }
    return size[u];
}

void decompose(int u, int t){
    top[u]=t;
    pos[u]=cur_pos++;
    if(heavy[u]) decompose(heavy[u], t);
    for(int i=head[u]; i!=-1; i=edges[i].next){
        int v = edges[i].to;
        if(v!=parent[u] && v!=heavy[u]) decompose(v,v);
    }
}

void build(int node, int l, int r, int val[]){
    if(l==r){ seg[node]=val[l]; return; }
    int m=(l+r)/2;
    build(node*2, l, m, val);
    build(node*2+1, m+1, r, val);
    seg[node]=max(seg[node*2], seg[node*2+1]);
}

void update(int node, int l, int r, int idx, int value){
    if(l==r){ seg[node]=value; return; }
    int m=(l+r)/2;
    if(idx<=m) update(node*2, l, m, idx, value);
    else update(node*2+1, m+1, r, idx, value);
    seg[node]=max(seg[node*2], seg[node*2+1]);
}

int query(int node, int l, int r, int ql, int qr){
    if(ql>r || qr<l) return 0;
    if(ql<=l && r<=qr) return seg[node];
    int m=(l+r)/2;
    return max(query(node*2,l,m,ql,qr), query(node*2+1,m+1,r,ql,qr));
}

int path_query(int u, int v){
    int res=0;
    while(top[u]!=top[v]){
        if(depth[top[u]]<depth[top[v]]) { int tmp=u; u=v; v=tmp; }
        res=max(res, query(1,0,cur_pos-1,pos[top[u]], pos[u]));
        u=parent[top[u]];
    }
    if(depth[u]>depth[v]) { int tmp=u; u=v; v=tmp; }
    if(pos[u]+1<=pos[v])
        res=max(res, query(1,0,cur_pos-1,pos[u]+1,pos[v]));
    return res;
}

int main(){
    int N;
    scanf("%d",&N);
    memset(head,-1,sizeof(head));
    int u,v,w;
    int val[MAXN];
    for(int i=1;i<N;i++){
        scanf("%d %d %d",&u,&v,&w);
        add_edge(u,v,i);
        add_edge(v,u,i);
        val[i]=w;
    }
    dfs(1);
    cur_pos=0;
    decompose(1,1);
    for(int i=1;i<N;i++){
        u=edges[(i-1)*2].to;
        v=edges[(i-1)*2+1].to;
        if(parent[v]==u) edge_to_node[i]=v;
        else edge_to_node[i]=u;
    }
    int seg_vals[MAXN];
    for(int i=1;i<N;i++)
        seg_vals[pos[edge_to_node[i]]]=val[i];
    build(1,0,cur_pos-1,seg_vals);
    
    int M;
    scanf("%d",&M);
    int cmd,idx,c,a,b;
    for(int i=0;i<M;i++){
        scanf("%d",&cmd);
        if(cmd==1){
            scanf("%d %d",&idx,&c);
            update(1,0,cur_pos-1,pos[edge_to_node[idx]],c);
        }else{
            scanf("%d %d",&a,&b);
            printf("%d\n",path_query(a,b));
        }
    }
    return 0;
}
