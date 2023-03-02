struct node *init(int value);
struct node *push(int value, struct node **end);
int pop(struct node **end);
void destroy(struct node *end);