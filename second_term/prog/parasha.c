#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>



struct node *init(int value);
struct node *push(int value, struct node **end);
int pop(struct node **end);
void destroy(struct node *end);

struct node{
	int data;
	struct node *next;
	struct node *prev;
};	

struct node *init(int value) {
    struct node *node;
    node = (struct node *)malloc(sizeof(struct node));
    node->data = value;
    node->next = NULL;
    node->prev = NULL;
    return node;
}

struct node *push(int value, struct node **end) {
    struct node *node;
    node = malloc(sizeof(struct node));
    node->data = value;
    node->next = NULL;
    node->prev = (*end);
    (*end) = node;
    return (*end);
}
int pop(struct node **end) {
    struct node *temp = *end;
    (*end) = (*end)->prev;
    (*end)->next = NULL;
    int result = temp->data;
    free(temp);
    return result;
}

void destroy(struct node *end) {
    while (end->prev) {
        pop(&end);
    }
    free(end);
}
