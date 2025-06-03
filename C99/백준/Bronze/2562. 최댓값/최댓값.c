#include <stdio.h>

int main() {
    int i, max, maxIndex;
    int list[9];
    
    max = 0;
    maxIndex = 0;
    
    for(i = 0; i < 9; i++) {
        scanf("%d", &list[i]);
    }
    
    for(i = 0; i < 9; i++) {
        if(list[i] > max) {
            max = list[i];
            maxIndex = i + 1;
        }
    }
    
    printf("%d\n", max);
    printf("%d", maxIndex);
}