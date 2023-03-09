#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "stack.h"

struct node{
    char data[8];
	struct node *prev;
};

struct node *stack = init();


void destroy_stack(){
    destroy(stack);
}

void push_stack(char *word){
    push(word, &stack);
}

void main(){
    push_stack("c");
    destroy_stack();
}
