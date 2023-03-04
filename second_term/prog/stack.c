#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>



struct node *init(char *word);
struct node *push(char *word, struct node **end);
char *pop(struct node **end);
void destroy(struct node *end);

struct node{
	char data[32];
	struct node *next;
	struct node *prev;
};	

struct node *init(char *word) {
    struct node *node;
    node = (struct node *)malloc(sizeof(struct node));
    printf("New word was added: %s\n", word);
    strcpy(node->data, word);
    node->next = NULL;
    node->prev = NULL;
    return node;
}

struct node *push(char *word, struct node **end) {
    struct node *node;
    node = malloc(sizeof(struct node));
    printf("New word was added: %s\n", word);
    strcpy(node->data, word);
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
    printf("%p Item that was deleted: %s\n", (*end), result);
    free(temp);
    return result;
}

void destroy(struct node *end) {
    while (end->prev) {
        pop(&end);
    }
    printf("stack was destroyed\n");
    free(end);
}
