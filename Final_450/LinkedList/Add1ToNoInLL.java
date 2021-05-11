/*
A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

Example 1:

Input:
LinkedList: 4->5->6
Output: 457 
Example 2:

Input:
LinkedList: 1->2->3
Output: 124 
Your Task:
Your task is to complete the function addOne() which takes the head of the linked list as the only argument and returns the head of the modified linked list. The driver code prints the number.
Note: The head represents the left-most digit of the number.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 101000
*/
public class Add1ToNoInLL {
    public static Node reverse(Node head) {
        Node prev = null;
        while (head != null) {
            Node vnext = head.next;
            head.next = prev;
            prev = head;
            head = vnext;
        }
        return prev;
    }

    public static Node addOne(Node head) {
        // code here.
        head = reverse(head);
        Node cur = head;

        while (cur != null) {
            if (cur.next == null && cur.data == 9) {
                cur.data = 1;
                Node temp = new Node(0);
                temp.next = head;
                head = temp;
                cur = cur.next;
            } else if (cur.data == 9) {
                cur.data = 0;
                cur = cur.next;
            } else {
                cur.data = cur.data + 1;
                cur = cur.next;
                break;
            }
        }
        head = reverse(head);
        return head;
    }
}