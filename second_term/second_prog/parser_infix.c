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

int next_token(token *t, char c, char *word) {
    if (isdigit(c)) {
        t->type = T_NUMBER;
        t->value = 0;
        do {
            t->value = t->value * 10 + (c - '0');
            word++;
            c = *word;
            printf("(%c): in loop\n", c);
        } while (isdigit(c));
        ungetc(c, stdin);

    } else if (c == '+' || c == '-' || c == '*' || c == '/') {
        printf("here operator");
        t->type = T_OPERATOR;
        t->value = c;

    } else if (c == '(' || c == ')') {
        t->type = T_BRACKET;
        t->value = c;

    } else if (c == '\n') {
        ungetc(c, stdin);
        return 0;
    }

    return 1;
}

int parse(char *word) {
    token t;
    FILE *file;
    file = fopen("txts/temp.txt", "w");
    int lines_count = 0;
    while (*word != '\0'){
        if (*word == ' '){
            word++;
            continue;
        }
        char c = *word;
        printf("%c\n", c);
        next_token(&t, c, word);
        lines_count++;
        switch (t.type) {
            case T_NUMBER:
                fprintf(file, "%d\n", t.value);
                break;
            case T_OPERATOR:
                fprintf(file, "%c\n", t.value);
                printf("here in case %c", t.value);
                break;
            case T_BRACKET:
                fprintf(file, "%c\n", t.value);
                break;
        }
        word++;        
    }
    fclose(file);
    return lines_count;
}
