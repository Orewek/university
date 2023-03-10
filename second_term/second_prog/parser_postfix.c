#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int parse(char *word){
    while (*word != '\0'){
        printf("%c", *word);
        word++;
    }
    printf("\n");
    return 0;
}