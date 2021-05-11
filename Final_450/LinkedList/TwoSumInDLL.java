public class TwoSumInDLL {
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

    public void twoSum(Node head, int k) {
        Node first = head;
        Node second = head;
        while (second.next != null) {
            second = second.next;
        }

        while (first != null && second != null && first != second && second.next != first) {
            if (first.data + second.data == k) {
                System.out.println(first.data + " " + second.data);
                first = first.next;
                second = second.prev;
            } else if (first.data + second.data > k) {
                second = second.prev;
            } else {
                first = first.next;
            }
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
        System.out.println();
    }

    public static void main(String[] args) {
        TwoSumInDLL m = new TwoSumInDLL();
        m.append(new Node(1));
        m.append(new Node(2));
        m.append(new Node(3));
        m.append(new Node(4));
        m.append(new Node(5));
        m.printDll(head);
        m.twoSum(head, 6);
        System.out.println(head.data);
    }

}
