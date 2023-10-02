#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - This prints all elements of a listint_t list
 * @h: The pointer to head of list
 * Return: The  number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* The number of nodes */

	current = h;
	n = 0;

	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}
	return (n);
}

/**
 * add_nodeint - The adds a new node at the beginning of a listint_t list
 * @head: The pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
 * free_listint - This frees a listint_t list
 * @head: The pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
