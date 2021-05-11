public class DelNodeInCLL {
    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    public void printLL(Node head) {
        Node temp = head;
        do {
            System.out.print(head.data + "->");
            head = head.next;
        } while (head != temp);
        System.out.println();
    }

    public Node remove(Node head, int rem) {
        Node fres = null;
        if (head.data == rem) {
            Node thead = head;
            Node temp = head.next;
            while (head.next != thead) {
                head = head.next;
            }
            head.next = head.next.next;
            fres = temp;
        } else {
            Node temp = head;
            while (temp.next.data != rem) {
                temp = temp.next;
            }
            temp.next = temp.next.next;
            fres = head;
        }
        return fres;
    }

    public static void main(String[] args) {
        DelNodeInCLL m = new DelNodeInCLL();
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = head;
        int rem = 2;
        m.printLL(head);
        m.printLL(m.remove(head, rem));
    }

}
