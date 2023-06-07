#include "lists.h"
/**
 * insert_node - inserts node in a sorted linked list
 * @head: the head of the list
 * @number: data element of the new node
 *
 * Return: the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	current = *head;
	prev = NULL;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		prev->next = new;
		new->next = current;
	}
	return (new);
}
