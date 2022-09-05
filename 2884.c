#include <stdio.h>

int H, M;

int main(){
    scanf("%d %d", &H, &M);
    if(H < 0 || H > 23) return 0;
    if(M < 0 || M > 59) return 0;

    if (M - 45 < 0){
        if ( H == 0) H = 24;
        H--;
        M = M + 15;
    }
    else if ( M - 45 >= 0){
        M = M - 45;
    }

    printf("%d %d", H, M);
    return 0;
}