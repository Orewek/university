#include <stdio.h>
#include <string.h>
#include <math.h>

#include "parasha.h"

int main(){
    struct node *balls = init(5);
    printf("%d", pop(&balls));

    return 0;
}