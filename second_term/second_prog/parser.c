#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define T_NUMBER 0
#define T_OPERATOR 1
#define T_BRACKET 2

typedef struct {
    int type;
    int value;
} token;

int next_token(token *t) {
    char c;

    do {
        c = getchar();
    } while (c == ' ');
    
    if (isdigit(c)) {
        t->type = T_NUMBER;
        t->value = 0;
        do {
            t->value = t->value * 10 + (c - '0');
            c = getchar();
        } while (isdigit(c));
        ungetc(c, stdin);

    } else if (c == '+' || c == '-' || c == '*' || c == '/') {
        t->type = T_OPERATOR;
        t->value = c;

    } else if (c == '(' || c == ')') {
        t->type = T_BRACKET;
        t->value = c;

    } else if (c == '\n') {
        ungetc(c, stdin);
        exit(0);

    }

    return 1;
}

void main() {
    token t;
    FILE *file;
    file = fopen("stack.txt", "w");
    while (next_token(&t)) {
        switch (t.type) {
            case T_NUMBER:
                fprintf(file, "%d\n", t.value);
                printf("number   %d\n", t.value);
                break;
            case T_OPERATOR:
                fprintf(file, "%c\n", t.value);
                printf("operator %c\n", t.value);
                break;
            case T_BRACKET:
                fprintf(file, "%c\n", t.value);
                printf("bracket  %c\n", t.value);
                break;
        }
    }
    fclose(file);
}