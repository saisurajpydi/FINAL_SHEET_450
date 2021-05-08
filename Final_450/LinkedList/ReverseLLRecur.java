public class ReverseLLRecur {
    static Node head;

    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    Node reverseLL(Node node) {
        if (node == null || node.next == null) {
            return node;
        }
        /*
         * reverse the rest list and put the first element at the end
         */
        Node rest = reverseLL(node.next);
        node.next.next = node;

        /* tricky step -- see the diagram */
        node.next = null;

        /* fix the head pointer */
        return rest;
    }

    void printLL(Node node) {
        while (node != null) {
            System.out.print(node.data + "->");
            node = node.next;
        }
        System.out.println();
    }

    public static void main(String args[]) {
        ReverseLLRecur list = new ReverseLLRecur();
        head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);

        list.printLL(head);
        list.printLL(list.reverseLL(head));
    }

}
