"""
Find first node of loop in a linked list
Difficulty Level : Medium
Last Updated : 05 Feb, 2021
Write a function findFirstLoopNode() that checks whether a given Linked List contains a loop. If the loop is present then it returns point to the first node of the loop. Else it returns NULL.

Example : 

Input : Head of below linked list
    head = newNode(1)
    head.next = newNode(2)
    head.next.next = newNode(3)
    head.next.next.next = newNode(4)
    head.next.next.next.next = newNode(5)
  
    # Create a loop for testing
    head.next.next.next.next.next = head.next.next

Output : Pointer to node 2

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def newNode(head):
    temp = Node(head)
    return temp


def printLL(head):
    while(head.next != None and head != None):
        print(head.data, "->", end=" ")
        head = head.next
    print()


def detectRemoveLoop(head):
    slow = head
    fast = head

    while(slow != None and fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next

        if(slow == fast):
            break

    if(slow == head):
        return head
    elif(slow == fast):
        slow = head
        while(slow.next != fast.next):
            slow = slow.next
            fast = fast.next
        return fast.next


if __name__ == "__main__":
    head = newNode(1)
    head.next = newNode(2)
    head.next.next = newNode(3)
    head.next.next.next = newNode(4)
    head.next.next.next.next = newNode(5)

    # Create a loop for testing
    head.next.next.next.next.next = head.next.next

    res = detectRemoveLoop(head)
    print("the first node of loop is :", res.data)
