#include <stdio.h>

int A, B, C, sum;

int cmp(int a, int b, int c){
    if (a == b){
        if (a == c) return 10000 + (a*1000);
        else return 1000+(a*100);
    }
    if (a != b){
        if (a == c) return 1000+(a*100);
        if (b == c) return 1000+(b*100);
        if (b != c) {
            if (a > b){
                if (a > c) return a*100;
                else return c*100;
            }
            else {
                if (b > c) return b*100;
                else return c*100;
            }
        }
    }
}

int main() {
    scanf("%d %d %d", &A, &B, &C);
    if(A < 1 || A > 6) return 0;
    if(B < 1 || B > 6) return 0;
    if(C < 1 || C > 6) return 0;

    sum = cmp(A, B, C);

    printf("%d", sum);
    return 0;
}