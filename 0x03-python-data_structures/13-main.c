#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_linked_list - print of linked list is a palindrome or not
 * @head: pointer to pointer of the first item in the linked list
 */
void check_linked_list(listint_t **head)
{
	if (is_palindrome(head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
}

/**
 * a2l - convert array into a linked list
 * @head: pointer to the linked list base (must be points to NULL)
 * @list: the data array to be converted
 * @size: the size of the array
 * Description:
 * The linked list must be empty to fill it
 */
void a2l(listint_t **head, int *list, int size)
{
	int i;

	if (!head || *head)
		return;

	for (i = 0; i < size; i++)
		add_nodeint_end(head, list[i]);
}

/**
 * test - start testing case
 * @data: the data array
 * @size: the size of the data array
 */
void test(int *data, int size)
{
	listint_t *head = NULL;

	a2l(&head, data, size);
	print_listint(head);
	check_linked_list(&head);
	free_listint(head);
	putchar(10);
}

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
		int data0[] = {1, 17, 972, 50, 98, 98, 50, 972, 17, 1};
		int data1[] = {1, 17, 972, 50, 98};
		int data2[] = {1};
		int data3[] = {1, 1};
		int data4[] = {1, 2};

		test(data0, 10);
		test(data1, 5);
		test(data2, 1);
		test(data3, 2);
		test(data4, 2);
		test(data4, 0);

		return (0);
}
