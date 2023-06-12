#include <stdio.h>
#include <stdlib.h>

typedef struct listint_t {
    int data;
    struct listint_t* next;
} listint_t;

int is_palindrome(listint_t** head) {
    listint_t* slow_ptr = *head;
    listint_t* fast_ptr = *head;
    listint_t* prev_slow_ptr = *head;
    listint_t* mid_node = NULL;
    int is_palindrome = 1;

    if (*head != NULL && (*head)->next != NULL) {
        // Find the middle of the linked list
        while (fast_ptr != NULL && fast_ptr->next != NULL) {
            fast_ptr = fast_ptr->next->next;
            prev_slow_ptr = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        // If the linked list has an odd number of nodes,
        // move slow_ptr to the next node
        if (fast_ptr != NULL) {
            mid_node = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        // Reverse the second half of the linked list
        listint_t* second_half = slow_ptr;
        prev_slow_ptr->next = NULL;
        reverse_list(&second_half);

        // Compare the first half and reversed second half of the linked list
        is_palindrome = compare_lists(*head, second_half);

        // Restore the original linked list by reversing the second half again
        reverse_list(&second_half);

        // If the linked list had an odd number of nodes, reconnect the middle node
        if (mid_node != NULL) {
            prev_slow_ptr->next = mid_node;
            mid_node->next = second_half;
        } else {
            prev_slow_ptr->next = second_half;
        }
    }

    return is_palindrome;
}

// Function to reverse a linked list
void reverse_list(listint_t** head) {
    listint_t* prev_node = NULL;
    listint_t* current_node = *head;
    listint_t* next_node = NULL;

    while (current_node != NULL) {
        next_node = current_node->next;
        current_node->next = prev_node;
        prev_node = current_node;
        current_node = next_node;
    }

    *head = prev_node;
}

// Function to compare two linked lists
int compare_lists(listint_t* head1, listint_t* head2) {
    listint_t* temp1 = head1;
    listint_t* temp2 = head2;

    while (temp1 != NULL && temp2 != NULL) {
        if (temp1->data != temp2->data) {
            return 0;
        }
        temp1 = temp1->next;
        temp2 = temp2->next;
    }

    return (temp1 == NULL && temp2 == NULL);
}

