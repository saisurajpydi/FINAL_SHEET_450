public class Cll {
    static class Node {
        int data;
        Node next;

        Node(int d) {

            data = d;
            next = null;
        }
    }

    void printCll(Node head) {
        Node temp = head;
        do {
            System.out.print(head.data + "->");
            head = head.next;
        } while (head != temp);
        System.out.println();

    }

    public static void main(String args[]) {
        Cll c = new Cll();
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = head;

        c.printCll(head);
    }

}
