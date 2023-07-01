#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define T_NUMBER 0
#define T_OPERATOR 1
#define T_BRACKET 2

// struct with type of value and value
typedef struct {
    int type;
    int value;
} token;

int next_token(token *t, char c, char *word) {
    /*
        Check if that is a digit
        Also need to check is that a number
        So if next char also a number:
        (digit1 * 10 + digit2)
    */
    if (isdigit(c)) {
        t->type = T_NUMBER;
        t->value = 0;
        do {
            t->value = t->value * 10 + (c - '0');
            word++;
            c = *word;
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
        return 0;
    }

    return 1;
}

void parse(char *word) {
    token t;
    FILE *file;
    file = fopen("txts/temp.txt", "w");
    while (*word != '\0') {
        // skipping spaces
        if (*word == ' ') {
            word++;
            continue;
        }
        char c = *word;
        next_token(&t, c, word);
        // adding a number/operand into additional line into .txt
        switch (t.type) {
            case T_NUMBER:
                fprintf(file, "%d\n", t.value);
                break;
            case T_OPERATOR:
                fprintf(file, "%c\n", t.value);
                break;
            case T_BRACKET:
                fprintf(file, "%c\n", t.value);
                break;
        }
        word++;
    }
    fclose(file);
}
