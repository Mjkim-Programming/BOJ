#include <stdio.h>

int main() {
    int nf, s;
    scanf("%d %d", &nf, &s);
    int ns = s * 2 - nf;
    
    printf("%d", ns);
    
    return 0;
}