#ifndef HEADER_H
#define HEADER_H
#include<stdio.h>
#include<stdlib.h>

//Node *add_node(node *head, char *name, int age);

typedef struct single
{
	char *name;
	int age;
        struct single *next;
}Node;

Node *add_node(Node *head, char *name, int age);
#endif
