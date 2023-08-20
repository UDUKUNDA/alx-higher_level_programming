#include "lists.h"
/**
 * check_cycle - this will see if the list has cycles
 * @list: the var
 *
 * Return: a value
 */
int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *l= list;

	if (!list)
	{
		return (0);
	}
	while (f && l && l->next)
	{
		f = f->next;
		l = l->next->next;
		if (f == l)
		{
			return (1);
		}
	}
	return (0);
}

