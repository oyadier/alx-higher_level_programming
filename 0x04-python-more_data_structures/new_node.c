#include "header.h"

Node *add_node(Node *head, char *name, int age)
{
	Node *newNode;

	newNode = malloc(sizeof(Node));
	if (newNode == NULL)
	{
		perror("malloc fail");
		exit(1);
	}

	newNode->name = name;
	newNode->age = age;
	newNode->next = head;//Which is NULL for the for beginning
	head = newNode;

	return head;

}


int main()
{

	Node *head = NULL;

	head = add_node(head, "Rober", 124);
	head = add_node(head, "Rd", 12);
	head = add_node(head, "Rodfeber", 112);
	head = add_node(head, "Roberd", 32);

	 Node* current = head;
    	while (current != NULL)
       	{
        	printf("%s : %d -> ", current->name, current->age);
        	current = current->next;
	}
	printf("NULL\n");
    return (0);

}


