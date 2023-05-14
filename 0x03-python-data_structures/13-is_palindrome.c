#include <stddef.h>
#include <limits.h>
#include "lists.h"

/**
 * find_next_node - find the next occurrence of the value of the @node in range
 * @node: the starting node
 * @index: the starting index
 * @last_index: the index to stop before
 * Return: returns the node if any otherwise NULL
 */
listint_t *find_next_node(listint_t *node, int *index, int last_index)
{
	int value = 0;

	if (!node)
		return (NULL);

	value = node->n;
	while (node->next && *index < last_index)
	{
		node = node->next;
		(*index)++;
		if (node->n == value)
			break;
	}
	if (node->n == value)
		return (node);
	return (NULL);
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
	listint_t *current_node = NULL, *last_node = NULL;
	int current_index = 0, last_index = INT_MAX, index = 0;

	if (!head || !*head)
		return (1);

	current_node = *head;
begin:
	index = current_index;
	last_node = find_next_node(current_node, &index, last_index);
	if (current_index >= last_index)
		return (1);
	if (!last_node || index > last_index)
		return (0);
	last_index = index;
	current_index++;
	current_node = current_node->next;
	goto begin;
}
