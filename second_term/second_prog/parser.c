#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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
    ungetc(c, stdin); /* save the non-digit for next time */

  } else if (c == '+' || c == '-' || c == '*' || c == '/') {
    t->type = T_OPERATOR;
    t->value = c;

  } else if (c == '(' || c == ')') {
    t->type = T_BRACKET;
    t->value = c;

  } else if (c == '\n') {
    ungetc(c, stdin);
    return 0;

  } else {

  }

  return 1;
}

int main() {

  token t;

  while (next_token(&t)) {
    switch (t.type) {
      case T_NUMBER:   printf("number   %d\n", t.value); break;
      case T_OPERATOR: printf("operator %c\n", t.value); break;
      case T_BRACKET:  printf("bracket  %c\n", t.value); break;
    }
  }

  return 0;
}