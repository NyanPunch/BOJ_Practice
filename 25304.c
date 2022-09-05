#include <stdio.h>

long long X, N, a, b, sum;

int main(){
    scanf("%lld", &X); if (X<0 || X> 1000000000) return 0;
    scanf("%lld", &N); if(N<0 || N>100) return 0;

    for(int i=0;i<N;i++){
        scanf("%d %d", &a, &b);
        sum += a*b;
    }
    if(X == sum) printf("Yes");
    else printf("No");

    return 0;
}