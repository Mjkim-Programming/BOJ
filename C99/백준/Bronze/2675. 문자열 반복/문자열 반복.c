#include <stdio.h>
#include <string.h>

int main() {
    int T;
    scanf("%d", &T);

    while(T--) {
        int R;
        char S[21];
        scanf("%d %s", &R, S);

        for(int i = 0; i < strlen(S); i++) {
            for(int j = 0; j < R; j++) {
                printf("%c", S[i]);
            }
        }
        printf("\n");
    }

    return 0;
}