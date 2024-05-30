#include <stdio.h>
#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle within.
*
* @list: singly linked list.
*
* Return: 0 ifno cycle exists.
*/
int check_cycle(listint_t *list)
{
	listint_t *head = NULL;
	listint_t *tail = NULL;

	if (!list)
		return (0);

	head = list;
	tail = list;

	while ((tail) && (tail->next))
	{
		head = head->next;
		tail = tail->next->next;

		if (head == tail)
			return (1);
	}
	return (0);
}
