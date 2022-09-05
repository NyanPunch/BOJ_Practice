#include <stdio.h>

int A, B;

int main() {
    while(scanf("%d %d", &A, &B) != -1){
        if(A<0||A>10 || B<0||B>10) break;
        printf("%d\n", A+B);
    }
    return 0;
}