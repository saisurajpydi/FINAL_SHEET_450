import java.util.*;
import java.io.*;

public class SortKSortedDLL {
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

    class compareNode implements Comparator<Node> {
        public int compare(Node n1, Node n2) {
            return n1.data - n2.data;
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

    public Node sort(Node head, int k) {
        if (head == null) {
            return head;
        }
        PriorityQueue<Node> pq = new PriorityQueue<>(new compareNode());
        Node nhead = null;
        Node cur = null;

        for (int i = 0; head != null && i <= k; i++) {
            pq.add(head);
            head = head.next;
        }
        while (!pq.isEmpty()) {
            if (nhead == null) {
                nhead = pq.peek();
                nhead.prev = null;
                cur = nhead;
            } else {
                cur.next = pq.peek();
                pq.peek().prev = cur;
                cur = pq.peek();
            }
            pq.poll();

            if (head != null) {
                pq.add(head);
                head = head.next;
            }
        }
        cur.next = null;

        return nhead;
    }

    public static void main(String[] args) {
        SortKSortedDLL m = new SortKSortedDLL();
        m.push(8);
        m.push(56);
        m.push(12);
        m.push(2);
        m.push(6);
        m.push(3);
        System.out.println("the given order");
        m.printDll(head);
        System.out.println("the sorted order");
        m.printDll(m.sort(head, 2));
    }
}
