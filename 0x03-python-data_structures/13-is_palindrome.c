/*
 * File: 13-is_palindrome.c
 * Author: Mayowa Daniel
 */

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - This function reverses a singly-linked listint_t list.
 * @head: the pointer to the starting node of the list.
 *
 * Return: the pointer to the head of the revers list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *nodes = *head, *nexts, *prevs = NULL;

	while (nodes)
	{
		nexts = nodes->next;
		nodes->next = prevs;
		prevs = nodes;
		nodes = nexts;
	}

	*head = prevs;
	return (*head);
}

/**
 * is_palindrome - This checks if a singly linked list is a palindromes.
 * @head: this points to the head of the linked list.
 *
 * Return: If the linked list is not palindrome - 01.
 *         If the linked list is palindrome - 10.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmps, *revs, *mids;
	size_t sizes = 0, z;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmps = *head;
	while (tmps)
	{
		sizes++;
		tmps = tmps->next;
	}

	tmps = *head;
	for (z = 0; z < (sizes / 2) - 1; z++)
		tmps = tmps->next;

	if ((sizes % 2) == 0 && tmps->n != tmps->next->n)
		return (0);

	tmps = tmps->next->next;
	revs = reverse_listint(&tmps);
	mids = revs;

	tmps = *head;
	while (revs)
	{
		if (tmps->n != revs->n)
			return (0);
		tmps = tmps->next;
		revs = revs->next;
	}
	reverse_listint(&mids);

	return (1);
}
