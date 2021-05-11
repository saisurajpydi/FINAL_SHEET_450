public class ImpleDLL {
    {
    static Node head = null;

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

    public void append(Node data) {
        Node cur = head;
        if (head == null) {
            head = data;
            head.next = null;
            head.prev = null;
        } else {
            while (cur.next != null) {
                cur = cur.next;
            }
            cur.next = data;
            data.prev = cur;
            data.next = null;
        }
    }

    public void push(Node data) {
        if (head == null) {
            head = data;
            head.next = null;
            head.prev = null;
        }
        // Node cur = head;
        data.next = head;
        head.prev = data;
        data.prev = null;
        head = data;
    }

    public void printDll(Node head) {
        while (head != null) {
            System.out.print(head.data + "<-->");
            head = head.next;
        }
    }

    public static void main(String[] args) {
        ImpleDLL m = new ImpleDLL();
        m.append(new Node(1));
        m.append(new Node(2));
        m.append(new Node(3));
        m.push(new Node(10));
        m.printDll(head);
    }
}