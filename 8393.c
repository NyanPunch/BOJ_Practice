#include <stdio.h>

int n;

int main(){
    scanf("%d",&n);
    if(n<0||n>10000) return 0;
    int sum = 0;
    for(int i=1;i<=n;i++){
        sum += i;
    }
    printf("%d", sum);
    return 0;
}