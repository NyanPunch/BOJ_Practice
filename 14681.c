#include <stdio.h>
//사분면
int X, Y;

int main(){
    scanf("%d %d", &X, &Y);
    if(X > 1000 && X < -1000 && X == 0) return 0;
    if(Y > 1000 && Y < -1000 && Y == 0) return 0;

    if(X > 0){
        if(Y > 0) printf("1");
        else if (Y < 0) printf("4");
    }
    else if (X < 0){
        if(Y > 0) printf("2");
        else if(Y<0) printf("3");
    }
    return 0;
}