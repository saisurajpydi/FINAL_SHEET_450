public class ReverseLLIter {
    static Node head;

    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    Node reverse(Node node) {
        Node prev = null;

        while (node != null) {
            Node vnext = node.next;
            node.next = prev;
            prev = node;
            node = vnext;
        }
        return prev;
    }

    public void printLL(Node node) {
        while (node != null) {
            System.out.print(node.data + "->");
            node = node.next;
        }
        System.out.println();
    }

    public static void main(String args[]) {
        ReverseLLIter list = new ReverseLLIter();
        head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);

        list.printLL(head);
        Node val = list.reverse(head);
        list.printLL(val);
    }

}
