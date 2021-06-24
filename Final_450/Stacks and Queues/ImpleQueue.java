
/*
 Queue | Set 1 (Introduction and Array Implementation)
Difficulty Level : Easy
Last Updated : 31 May, 2021
Like Stack, Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO).  A good example of queue is any queue of consumers for a resource where the consumer that came first is served first. 
The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.
Operations on Queue: 
Mainly the following four basic operations are performed on queue:
Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition. 
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition. 
Front: Get the front item from queue. 
Rear: Get the last item from queue. 
 
 */
import java.util.*;

public class ImpleQueue {
    static int n;
    static ArrayList<Integer> alist;
    int front;
    int rear;

    static void enq(int val) {
        if (alist.size() < n) {
            alist.add(val);
        } else {
            System.out.println("the size is full");
        }
    }

    static void deq() {
        if (alist.size() != 0) {
            alist.remove(0);
        } else {
            System.out.println("the queue is empty, can't dequeue");
        }
    }

    static void front() {
        System.out.print("\nthe front element is " + alist.get(0));
    }

    static void rear() {
        System.out.print("\nthe rear element is " + alist.get(alist.size() - 1));
    }

    static void printQueue() {
        for (int i : alist) {
            System.out.print(i + " ");
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        alist = new ArrayList<>(n);
        enq(10);
        enq(11);
        enq(12);
        enq(13);
        printQueue();
        deq();
        deq();
        deq();
        front();
        rear();
        printQueue();
    }

}
