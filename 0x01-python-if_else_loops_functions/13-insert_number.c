#include "lists.h"
/**
 * insert_node - This function Inserts a number into a sorted
 * singly-linked list.
 * @head: The pointer the head of the linked list.
 * @number: This is the number to insert.
 *
 * Return: 0 If it fails - NULL. Otherwise  pointer to the node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *news;

	news = malloc(sizeof(listint_t));
	if (news == NULL)
		return (NULL);
	news->n = number;

	if (node == NULL || node->n >= number)
	{
		news->next = node;
		*head = news;
		return (news);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	news->next = node->next;
	node->next = news;

	return (news);
}
