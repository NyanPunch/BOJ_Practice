#include <stdio.h>

int N;

int main(){
    scanf("%d", &N);

    for(int i=0;i<N;i++){
        for(int j=0;j<=i;j++) printf("*");
        printf("\n");
    }
}