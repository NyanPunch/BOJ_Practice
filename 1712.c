#include <stdio.h>
//A = 고정비용, B = 가변비용, C = 개당판매비용
int A, B, C;

int main(){

    scanf("%d %d %d", &A, &B, &C);

    if(B>=C) printf("-1");
    else printf("%d", A/(C-B) + 1);

    return 0;
}