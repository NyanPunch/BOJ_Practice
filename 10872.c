#include <stdio.h>

int N, ans=1;

void fact(int n){
    if(n<0||n>12) return;

    for(int i=n; i>0;i--){
        ans *= i;
    }
    printf("%d", ans);
}

int main(){
    scanf("%d",&N);

    fact(N);
    return 0;
}