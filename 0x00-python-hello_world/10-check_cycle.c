#include "lists.h"
/**
 * check_cycle - This function checks if a linked list contain a cycle
 * @list: the linked lidt to be checked
 * written by mayowa dan
 * Return: 0 if it doent and 1 if it does
 */
int check_cycle(listint_t *list)
{
	listint_t *slows = list;
	listint_t *fasts = list;

	if (!list)
		return (0);

	while (slows && fasts && fasts->next)
	{
		slows = slows->next;
		fasts = fasts->next->next;

		if (slows == fasts)
			return (1);
	}
	return (0);
}
