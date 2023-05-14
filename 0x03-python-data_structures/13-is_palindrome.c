#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first linked list item pointer
 * Description:
 * Note: empty list and Null head also considered a palindrome case
 * Return: 0 is the list is not a palindrome otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current_node = NULL, *searching_node = NULL, *last_node = NULL;

	if (!head || !*head || !(*head)->next)
		return (1);
	current_node = *head;
loop:
	if (current_node == last_node)
		return (1);
	searching_node = current_node;
	while (searching_node->next && searching_node != last_node)
	{
		searching_node = searching_node->next;
		if (searching_node->n == current_node->n)
			break;
	}
	if (searching_node->n != current_node->n)
		return (0);
	last_node = searching_node;
	current_node = current_node->next;
	goto loop;
}
