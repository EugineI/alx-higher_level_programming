#include "lists.h"
/**
 * reverse_list - Reverses the list
 * @head: head of the list
 * Return: pointer to first node of reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *new = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = new;
		new = current;
		current = next;
	}
	return (new);
}
/**
 * is_palindrome - checks for palindrome
 * @head: pointer to head
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second, *prev_slow, *mid_node, *first, *second_copy;
	int result;

	if (head == NULL || *head == NULL)
		return (1);
	slow = *head;
	fast = *head;
	prev_slow = *head;
	mid_node = NULL;
	result = 1;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}
	second = reverse_list(slow);
	prev_slow->next = NULL;
	first = *head;
	second_copy = second;
	while (second != NULL)
	{
		if (first->n != second->n)
		{
			result = 0;
			break;
		}
		first = first->next;
		second = second->next;
	}
	second = reverse_list(second_copy);
	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second;
	}
	else
		prev_slow->next = second;
	return (result);
}
