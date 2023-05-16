#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * listlen - count the number of nodes inside a linked list
 * @node: pointer to the first list node
 * Return: the number of nodes
 */
long listlen(listint_t *node)
{
	long count = 0;

	while (node)
	{
		count++;
		node = node->next;
	}
	return (count);
}

/**
 * getat - get a linked list node at index
 * @head: pointer to the first list node
 * @index: the index of the node after the @head node
 */
listint_t *getat(listint_t *head, long index)
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
	listint_t *curr = NULL;
	int *nums = NULL;

	if (!head || !*head)
		return (1);
	len = listlen(*head);
	nums = malloc(sizeof(int) * len);
	if (!nums)
		return (1);
	curr = *head;

	for (i = 0; i < len; i++, curr = curr->next)
		nums[i] = curr->n;

	for (i = 0; i < len / 2; i++)
		if (nums[i] != nums[len - i - 1])
		{
			free(nums);
			return (0);
		}

	free(nums);
	return (1);
}
