
/**
 * 
 */
import java.util.*;

public class ImpleStackUseQueue {
    static Queue<Integer> q1 = new LinkedList<Integer>();
    static Queue<Integer> q2 = new LinkedList<Integer>();

    // Function to push an element into stack using two queues.
    static void push(int x) {
        // Your code here
        q2.add(x);

        while (!q1.isEmpty()) {
            q2.add(q1.peek());
            q1.remove();
        }

        // swap the names of two queues
        Queue<Integer> q = q1;
        q1 = q2;
        q2 = q;
    }

    // Function to pop an element from stack using two queues.
    static int pop() {
        if (q1.isEmpty()) {
            return -1;
        }
        return q1.remove();
    }

    public static void main(String args[]) {
        push(1);
        push(2);
        push(3);
        push(4);
        System.out.println(pop());
        System.out.println(pop());

    }
}
