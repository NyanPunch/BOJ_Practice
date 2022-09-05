#include <stdio.h>
//윤년
int N;

int main() {
    scanf("%d", &N);
    if( N < 1 || 4000 < N ) return 0;
    if(N % 4 == 0) {
        if(N % 400 == 0) printf("1");
        else if ( N % 100 != 0) printf("1");
        else printf("0");
    }
    else printf("0");
    
    return 0;
}