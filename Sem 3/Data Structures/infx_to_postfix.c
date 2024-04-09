#include <stdio.h>
#include <conio.h>
#include <string.h>

char stack[20], expr[20];
int c=0, top=-1;

void push(char);
void pop();
int priority(char);
void postfix();

int main() {
    printf("Enter an infix expression: ");
    scanf("%s", expr);
    printf("Postfix expression: ");
    while (c < strlen(expr)) {
        postfix();
    }

    while (top != -1) {
        printf("%c", stack[top]);
        pop();
    }
    return 0;
}

void push(char x) {
    top++;
    stack[top] = x;
}

void pop() {
    if (top == -1) {
        printf("Invalid expression");
    } 
    top--;
}

int priority(char x) {
    if (x == '^') {
        return 5;
    } else if (x == '*' || x == '/' || x == '%') {
        return 4;
    } else if (x == '+' || x == '-') {
        return 3;
    } else if (x == '(') {
        return 2;
    }
    return 0;
}

void postfix() {
    if (expr[c] == '+' || expr[c] == '-' || expr[c] == '/' || expr[c] == '*' || expr[c] == '%' || expr[c] == "^") {
        while (top != -1 && priority(expr[c]) <= priority(stack[top])) {
            printf("%c", stack[top]);
            pop();
        }
        push(expr[c]);
        c++;
    } else if (expr[c] == '(') {
        push(expr[c]);
        c++;
    } else if (expr[c] == ')') {
        while (stack[top] != '(') {
            printf("%c", stack[top]);
            pop();
        }
        pop();
        c++;
    } else {
        printf("%c", expr[c]);
        c++;
    }
}