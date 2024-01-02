#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts into a sorted linked list.
 *
 * @head: list head
 * @number: number to store in the newList node
 *
 * Return: pointer to the newList node
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *runner = NULL;
        listint_t *newList  = NULL;

        runner = *head;

        newList = malloc(sizeof(listint_t));
        if (!newList)
                return (NULL);
        newList->n = number;

        if ((!(*head)) || ((*head)->n > number))
        {
                newList->next = *head;
                *head = newList;
                return (newList);
        }

        while (runner->next)
        {
                if ((runner->next)->n >= number)
                {
                        newList->next = runner->next;
                        runner->next = newList;
                        return (newList);
                }
                runner = runner->next;
        }

        newList->next = NULL;
        runner->next = newList;
        return (newList);
}
