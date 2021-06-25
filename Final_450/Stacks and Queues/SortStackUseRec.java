
/**
 * Sort a stack 
Easy Accuracy: 50.51% Submissions: 44668 Points: 2
Given a stack, the task is to sort it such that the top of the stack has the greatest element.

Example 1:

Input:
Stack: 3 2 1
Output: 3 2 1
Example 2:

Input:
Stack: 11 2 32 3 41
Output: 41 32 11 3 2
Your Task: 
You don't have to read input or print anything. Your task is to complete the function sort() which sorts the elements present in the given stack. (The sorted stack is printed by the driver's code by popping the elements of the stack.)

Expected Time Complexity : O(N*N)
Expected Auixilliary Space : O(N) recursive.

Constraints:
1<=N<=100

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.


 */
import java.util.*;

public class SortStackUseRec {
    static Stack<Integer> s = new Stack<>();

    public static void rec(Stack<Integer> s, int N) {
        if (s.isEmpty() || N > s.peek()) {
            s.push(N);
            return;
        }
        int temp = s.pop();
        rec(s, N);
        s.push(temp);

    }

    public Stack<Integer> sort(Stack<Integer> s) {
        // add code here.
        if (!s.isEmpty()) {
            int x = s.pop();
            sort(s);
            rec(s, x);
        }
        return s;
    }

    public static void main(String args[]) {
        SortStackUseRec m = new SortStackUseRec();
        s.push(11);
        s.push(10);
        s.push(9);
        s.push(8);
        s.push(7);
        System.out.println(s);
        System.out.println("after sort ");
        System.out.println(m.sort(s));
    }
}
