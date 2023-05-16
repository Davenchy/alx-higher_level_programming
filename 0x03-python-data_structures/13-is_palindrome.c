#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * listlen - count the number of nodes inside a linked list
 * @node: pointer to the first list node
 * Return: the number of nodes
 */
size_t listlen(listint_t *node)
{
	size_t count = 0;

	if (!node)
		goto end;

	do {
		count++;
		node = node->next;
	} while(node);
end:
	return (count);
}

/**
 * getat - get a linked list node at index
 * @head: pointer to the first list node
 * @index: the index of the node after the @head node
 */
listint_t *getat(listint_t *head, size_t index)
{
	while (index && head)
	{
		head = head->next;
		index--;
	}
	if (index)
		head = NULL;
	return (head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first linked list item pointer
 * Description:
 * Note: empty list and Null head also considered a palindrome case
 * Return: 0 is the list is not a palindrome otherwise 1
 */
int is_palindrome(listint_t **head)
{
	size_t i = 0, len = 0;

	if (!head || !*head)
		return (1);
	len = listlen(*head);

	for (i = 0; i < len/2; i++)
	{
		listint_t *a, *b;

		a = getat(*head, i), b = getat(*head, len - i - 1);
		if (a->n != b->n)
			return (0);
	}
	return (1);
}
