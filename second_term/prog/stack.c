#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct node *init();
struct node *push(char *word, struct node **end);
char *pop(struct node **end);
void destroy(struct node *end);

struct node{
	char data[32];
	struct node *next;
	struct node *prev;
};

struct node *init() {
    struct node *node;
    node = (struct node *)malloc(sizeof(struct node));
    strcpy(node->data, "None");
    node->next = NULL;
    node->prev = NULL;
    return node;
}

struct node *push(char *word, struct node **end) {
    struct node *node;
    node = malloc(sizeof(struct node));
    strcpy(node->data, word);
    printf("New word was added: %s\n", word);
    node->next = NULL;
    node->prev = (*end);
    (*end) = node;
    return (*end);
}
char *pop(struct node **end) {
    struct node *temp = *end;
    (*end) = (*end)->prev;
    (*end)->next = NULL;
    char *result = temp->data;
    printf("Item that was deleted: %s\n", result);
    free(temp);
    return result;
}

void destroy(struct node *end) {
    while (end->prev) {
        pop(&end);
    }
    printf("STACK WAS DESTROYED\n");
    free(end);
}
