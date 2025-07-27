#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int max, min;
    max = -1000000;
    min = 1000000;
    
    int arr[n];
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    for(int i = 0; i < n; i++) {
        if(arr[i] > max) {
            max = arr[i];
        }
        if(arr[i] < min) {
            min = arr[i];
        }
    }
    
    printf("%d %d", min, max);
}