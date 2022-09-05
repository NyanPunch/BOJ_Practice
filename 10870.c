//피보나치

#include <stdio.h>

int N, ans;

/*
int fibonacci(int a){
    if(a == N) return ans; //종료조건
    if (a == 0) ans = 0; // 0번째
    if (a == 1) ans = 1; // 1번째
    //2번부터 공식 사용 
    if(a >= 2) {
        ans  = fibonacci(a-1) + fibonacci(a-2);
        printf("fibonacci %d", ans);
    }

    return fibonacci(a++);
}
*/

int fibo(int a){
    if (a<=1) return a;
    else return fibo(a-1) + fibo(a-2);
}

int main() {

    scanf("%d",&N);

    printf("%d",fibo(N));

    return 0;
}