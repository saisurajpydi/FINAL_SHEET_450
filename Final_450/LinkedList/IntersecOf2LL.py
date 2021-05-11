"""
Given two lists sorted in increasing order, create a new list representing the intersection of the two lists. The new list should be made with its own memory — the original lists should not be changed.

Example 1:

Input:
L1 = 1->2->3->4->6
L2 = 2->4->6->8
Output: 2 4 6
Explanation: For the given first two
linked list, 2, 4 and 6 are the elements
in the intersection.
Example 2:

Input:
L1 = 10->20->40->50
L2 = 15->40
Output: 40
Your Task:
The task is to complete the function intersection() which should find the intersection of two linked list and add all the elements in intersection to the third linked list and return the head of the third linked list.

Expected Time Complexity : O(n+m)
Expected Auxilliary Space : O(n+m)
Note: n,m are the size of the linked lists.

Constraints:
1 <= size of linked lists <= 5000
1 <= Data in linked list nodes <= 1000
"""


def findIntersection(head1, head2):
    # return head
    result = list()
    while(head1 != None and head2 != None):
        if(head1.data < head2.data):
            head1 = head1.next
        elif(head1.data > head2.data):
            head2 = head2.next
        else:
            result.append(head1.data)
            head1 = head1.next
            head2 = head2.next

    head = Node(result[0])
    temp = head
    for i in range(1, len(result)):
        head.next = Node(result[i])
        head = head.next
    return temp
