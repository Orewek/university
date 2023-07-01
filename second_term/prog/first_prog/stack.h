struct node *init();
struct node *push(char *word, struct node **end);
char *pop(struct node **end);
void destroy(struct node *end);