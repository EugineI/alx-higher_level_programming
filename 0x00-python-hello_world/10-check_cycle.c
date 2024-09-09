#include"lists.h"
/**
 * check_cycle - check if there is a cycle
 * @list: list to be checked
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);
}
