
/**
 * Design a stack with operations on middle element
Difficulty Level : Medium
Last Updated : 31 May, 2021
How to implement a stack which will support following operations in O(1) time complexity? 
1) push() which adds an element to the top of stack. 
2) pop() which removes an element from top of stack. 
3) findMiddle() which will return middle element of the stack. 
4) deleteMiddle() which will delete the middle element. 
Push and pop are standard stack operations. 
The important question is, whether to use a linked list or array for implementation of stack? 
Please note that, we need to find and delete middle element. Deleting an element from middle is not O(1) for array. Also, we may need to move the middle pointer up when we push an element and move down when we pop(). In singly linked list, moving middle pointer in both directions is not possible. 
The idea is to use Doubly Linked List (DLL). We can delete middle element in O(1) time by maintaining mid pointer. We can move mid pointer in both directions using previous and next pointers. 
Following is implementation of push(), pop() and findMiddle() operations. Implementation of deleteMiddle() is left as an exercise. If there are even elements in stack, findMiddle() returns the second middle element. For example, if stack contains {1, 2, 3, 4}, then findMiddle() would return 3. 
 */
import java.util.*;

public class StackWithOpOnMid {
    static ArrayList<Integer> alist = new ArrayList<>();

    static void push(int val) {
        alist.add(val);
    }

    static void peek() {
        System.out.println("the peek ele is " + alist.get(alist.size() - 1));
    }

    static void pop() {
        alist.remove(alist.size() - 1);
    }

    static void mid() {
        int mid = (int) (alist.size()) / 2;
        System.out.println("the mid element is :" + alist.get(mid));
    }

    public static void main(String args[]) {
        push(10);
        push(11);
        push(12);
        push(13);
        push(14);
        mid();
        peek();
        pop();
        mid();
        peek();
        pop();
        mid();
    }
}

// public class GFG {
// /* A Doubly Linked List Node */
// class DLLNode {
// DLLNode prev;
// int data;
// DLLNode next;
// DLLNode(int d) { data = d; }
// }

// /* Representation of the stack data structure that
// supports findMiddle() in O(1) time. The Stack is
// implemented using Doubly Linked List. It maintains
// pointer to head node, pointer to middle node and
// count of nodes */
// class myStack {
// DLLNode head;
// DLLNode mid;
// int count;
// }

// /* Function to create the stack data structure */
// myStack createMyStack()
// {
// myStack ms = new myStack();
// ms.count = 0;
// return ms;
// }

// /* Function to push an element to the stack */
// void push(myStack ms, int new_data)
// {

// /* allocate DLLNode and put in data */
// DLLNode new_DLLNode = new DLLNode(new_data);

// /* Since we are adding at the beginning,
// prev is always NULL */
// new_DLLNode.prev = null;

// /* link the old list off the new DLLNode */
// new_DLLNode.next = ms.head;

// /* Increment count of items in stack */
// ms.count += 1;

// /* Change mid pointer in two cases
// 1) Linked List is empty
// 2) Number of nodes in linked list is odd */
// if (ms.count == 1) {
// ms.mid = new_DLLNode;
// }
// else {
// ms.head.prev = new_DLLNode;

// if ((ms.count % 2)
// != 0) // Update mid if ms->count is odd
// ms.mid = ms.mid.prev;
// }

// /* move head to point to the new DLLNode */
// ms.head = new_DLLNode;
// }

// /* Function to pop an element from stack */
// int pop(myStack ms)
// {
// /* Stack underflow */
// if (ms.count == 0) {
// System.out.println("Stack is empty");
// return -1;
// }

// DLLNode head = ms.head;
// int item = head.data;
// ms.head = head.next;

// // If linked list doesn't become empty, update prev
// // of new head as NULL
// if (ms.head != null)
// ms.head.prev = null;

// ms.count -= 1;

// // update the mid pointer when we have even number
// // of elements in the stack, i,e move down the mid
// // pointer.
// if (ms.count % 2 == 0)
// ms.mid = ms.mid.next;

// return item;
// }

// // Function for finding middle of the stack
// int findMiddle(myStack ms)
// {
// if (ms.count == 0) {
// System.out.println("Stack is empty now");
// return -1;
// }
// return ms.mid.data;
// }

// // Driver program to test functions of myStack
// public static void main(String args[])
// {
// GFG ob = new GFG();
// myStack ms = ob.createMyStack();
// ob.push(ms, 11);
// ob.push(ms, 22);
// ob.push(ms, 33);
// ob.push(ms, 44);
// ob.push(ms, 55);
// ob.push(ms, 66);
// ob.push(ms, 77);

// System.out.println("Item popped is " + ob.pop(ms));
// System.out.println("Item popped is " + ob.pop(ms));
// System.out.println("Middle Element is "
// + ob.findMiddle(ms));
// }
// }

// This code is contributed by Sumit Ghosh
