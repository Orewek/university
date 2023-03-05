#define  _GNU_SOURCE

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#include "stack.h"

int main(){
    FILE *file;
    char line[32] = {0};

    struct node *input_stack = init();
    struct node *result_stack = init();

    file = fopen("students.txt", "r");
    if (NULL == file){
        printf("cant find this .txt file!");
        exit(0);
    }
    int lines_count = 0;
    while (fgets(line, 32, file)){
        push(line, &input_stack);
        lines_count++;
    }
    fclose(file);


    
    destroy(result_stack);
    destroy(input_stack);
    
    return 0;
}
