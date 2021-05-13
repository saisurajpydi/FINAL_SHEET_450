public class ReverseDllInGrps {
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

    void printDll(Node head) {
        Node cur = head;
        while (cur != null) {
            System.out.print(cur.data + "<-->");
            cur = cur.next;
        }
        System.out.println();
    }

    void append(int v) {
        Node val = new Node(v);
        if (head == null) {
            head = val;
        }
        Node cur = head;
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = val;
        val.prev = cur;
        val.next = null;
    }

    public Node reverseDLL(Node head, int k) {
        Node vnext = null;
        Node vprev = null;
        Node cur = head;
        int c = 0;
        while (cur != null && c != k) {
            vnext = cur.next;
            cur.next = vprev;
            vprev = cur;
            cur = vnext;

            c += 1;
        }
        if (vnext != null) {
            head.next = reverseDLL(vnext, k);
        }
        return vprev;
    }

    public static void main(String[] args) {
        ReverseDllInGrps m = new ReverseDllInGrps();
        // head = new Node(1);
        m.append(1);
        m.append(2);
        m.append(3);
        m.append(4);
        m.append(5);
        System.out.println("the order is ");
        m.printDll(head);
        System.out.println("after reversing in grps ");
        m.printDll(m.reverseDLL(head, 3));
    }
}
