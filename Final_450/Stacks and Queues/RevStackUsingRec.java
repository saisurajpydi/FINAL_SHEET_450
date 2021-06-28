
/**
 * Reverse a stack using recursion
Difficulty Level : Medium
Last Updated : 30 Oct, 2020
Write a program to reverse a stack using recursion. You are not allowed to use loop constructs like while, for..etc, and you can only use the following ADT functions on Stack S: 
isEmpty(S) 
push(S) 
pop(S)

Recommended: Please try your approach on {IDE} first, before moving on to the solution.
The idea of the solution is to hold all values in Function Call Stack until the stack becomes empty. When the stack becomes empty, insert all held items one by one at the bottom of the stack. 
For example, let the input stack be  

    1  <-- top
    2
    3
    4    
First 4 is inserted at the bottom.
    4 <-- top

Then 3 is inserted at the bottom
    4 <-- top    
    3

Then 2 is inserted at the bottom
    4 <-- top    
    3 
    2
     
Then 1 is inserted at the bottom
    4 <-- top    
    3 
    2
    1
So we need a function that inserts at the bottom of a stack using the above given basic stack function.
void insertAtBottom((): First pops all stack items and stores the popped item in function call stack using recursion. And when stack becomes empty, pushes new item and all items stored in call stack.
void reverse(): This function mainly uses insertAtBottom() to pop all items one by one and insert the popped items at the bottom.  
 */
import java.util.*;

public class RevStackUsingRec {
    static Stack<Character> stack = new Stack<>();

    static void insertAtBottom(char x) {
        if (stack.isEmpty()) {
            stack.push(x);
        } else {
            char a = stack.peek();
            stack.pop();
            insertAtBottom(x);
            stack.push(a);
        }
    }

    static void reverse() {
        if (stack.size() > 0) {
            char x = stack.peek();
            stack.pop();
            reverse();
            insertAtBottom(x);

        }

    }

    public static void main(String args[]) {
        stack.push('1');
        stack.push('2');
        stack.push('3');
        stack.push('4');
        System.out.println("before reverse");
        System.out.println(stack);
        reverse();
        System.out.println("after reverse");
        System.out.println(stack);
    }
}
