public class RotateDllByNInACW {
    static Node head;

    static class Node {
        int data;
        Node next;
        Node prev;

        Node(int d) {
            data = d;
            next = null;
            prev = null;
        }
    }

    void push(int v) {
        Node val = new Node(v);
        if (head == null) {
            head = val;
        } else {
            head.prev = val;
            val.next = head;
            val.prev = null;
            head = val;
        }
    }

    void printDll(Node head) {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + "<-->");
            temp = temp.next;
        }
        System.out.println();
    }

    public Node rotate(Node head, int k) {
        Node cur = head;
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = head;
        head.prev = cur;
        Node temp = head;
        while (k != 0) {
            temp = head;
            head = head.next;
            k -= 1;
        }
        temp.next = null;

        return head;
    }

    public static void main(String[] args) {
        RotateDllByNInACW m = new RotateDllByNInACW();
        m.push(6);
        m.push(5);
        m.push(4);
        m.push(3);
        m.push(2);
        m.push(1);
        System.out.println("the given order");
        m.printDll(head);
        System.out.println("the rotated order");
        m.printDll(m.rotate(head, 4));
    }

}
