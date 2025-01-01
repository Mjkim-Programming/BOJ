#include <stdio.h>

int main() {
    int hour, minute;
    scanf("%d %d", &hour, &minute);
    
    minute -= 45;
    if(minute < 0) {
        minute += 60;
        hour -= 1;
        
        if (hour == -1){
            hour = 23;
        }
    }
    
    printf("%d %d", hour, minute);
    
    return 0;
}