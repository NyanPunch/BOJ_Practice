#include <stdio.h>

int H, M, T;

int main() {
    int a, b;
    scanf("%d %d", &H, &M);
    scanf("%d", &T);
    if(H < 0 || H > 23 || M < 0 || M > 59) return 0;
    if(T < 0 || T > 1000) return 0;

    H += T / 60;
    M += T % 60;

    if (M >= 60){
        H++;
        M -= 60;
    }
    if ( H >= 24){
        H -= 24;
    }

    printf("%d %d", H, M);
    return 0;
}