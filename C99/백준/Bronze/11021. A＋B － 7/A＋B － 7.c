#include <stdio.h>

int main() {
    int a, b, x;
    scanf("%d", &x);
    
    for(int i = 1; i <= x; i++) {
        scanf("%d %d", &a, &b);
        printf("Case #%d: %d\n", i, a+b);
    }
}