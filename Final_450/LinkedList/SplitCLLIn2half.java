public class SplitCLLIn2half {
    void splitList(circular_LinkedList list) {
        // Your code here
        Node head = list.head;
        Node head1 = list.head1;
        Node head2 = list.head2;
        Node slow = head;
        Node fast = head.next;
        while (fast != head && fast.next != head) {
            slow = slow.next;
            fast = fast.next.next;
        }
        head1 = head;
        head2 = slow.next;
        slow.next = head1;
        Node cur = head2;
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = head2;
    }

}
