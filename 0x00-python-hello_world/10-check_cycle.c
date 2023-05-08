#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle
 * @list: pointer to the first node in the linked list
 * Return: 0 if there is no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);

	slow = list, fast = list->next;

	while (fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
