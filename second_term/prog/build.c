#define  _GNU_SOURCE

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#include "stack.h"

struct node{
	char data[32];
	struct node *prev;
};

int main(){
    FILE *file;
    char line[32] = {0};

    struct node *input_stack = init();
    struct node *result_stack = init();

    file = fopen("studentss.txt", "r");
    if (NULL == file){
        printf("cant find this .txt file!");
        exit(0);
    }
    while (fgets(line, 32, file)){
        push(line, &input_stack);
    }
    fclose(file);

    while(input_stack->prev != NULL){
        char temp_data[32];
        strcpy(temp_data, input_stack->data);
        pop(&input_stack);
        
        while (result_stack->prev != NULL && strcmp(result_stack->data, temp_data) > 0){
            char temp2_data[32];
            strcpy(temp2_data, result_stack->data);
            pop(&result_stack); 
            push(temp2_data, &input_stack);
        }

        push(temp_data, &result_stack);
    }
     
    FILE *res_file;
    res_file = fopen("copy.txt", "w");
    while (result_stack->prev != NULL){
        char final_data[32];
        strcpy(final_data, result_stack->data);
        pop(&result_stack);
        fputs(final_data, res_file);
    }

    fclose(res_file);
    remove("students.txt");
    rename("copy.txt", "students.txt");

    remove("copy.txt");


    destroy(result_stack);
    destroy(input_stack);
    
    return 0;
}
