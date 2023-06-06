#include "lists.h"
/**
 * check_cycle - checks if there is loop in a linked list
 * @list: the head of the linked lisrt
 * Return: 0 if there is no loop and 1 if a loop is found
 */

int check_cycle(listint_t *list)
{
	listint_t *ferrari, *beetle;

	ferrari = list;
	beetle = list;

	while (ferrari != NULL && beetle != NULL && ferrari->next != NULL)
	{
		beetle = beetle->next;
		ferrari = (ferrari->next)->next;

		if (beetle == ferrari)
			return (1);
		if (ferrari == NULL)
			return (0);
	}
	return (0);
}
