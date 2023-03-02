#define  _GNU_SOURCE

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#include "stack.h"

int main(){
    FILE *file;
    char line[32] = {0};
    size_t len = 0;
    ssize_t read;
    struct node *student_stack = init("#");

    file = fopen("students.txt", "r");
    if (NULL == file){
        printf("cant find this .txt file!");
        exit(0);
    }
    while (fgets(line, 32, file)){
        push(line, &student_stack);
    }
    fclose(file);
    destroy(student_stack);
    
    return 0;
}