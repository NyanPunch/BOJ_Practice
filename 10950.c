#include <stdio.h>

int A[10], B[10], T;

int main() {
    scanf("%d",&T);
    for(int i=0; i<T; i++){
        scanf("%d %d", &A[i], &B[i]);
        printf("%d\n", A[i]+B[i]);
    }
    return 0;
}