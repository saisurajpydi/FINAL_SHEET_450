
/**
 * Valid Substring 
Easy Accuracy: 48.25% Submissions: 17680 Points: 2
Given a string S consisting only of opening and closing parenthesis 'ie '('  and ')', find out the length of the longest valid(well-formed) parentheses substring.
NOTE: Length of smallest the valid substring ( ) is 2.

Example 1:

Input: S = "(()("
Output: 2
Explanation: The longest valid 
substring is "()". Length = 2.
Example 2:

Input: S = "()(())("
Output: 6
Explanation: The longest valid 
substring is "()(())". Length = 6.

Your Task:  
You dont need to read input or print anything. Complete the function findMaxLen() which takes S as input parameter and returns the maxlength.


Expected Time Complexity:O(n)
Expected Auxiliary Space: O(1)   


Constraints:
1 <= |S| <= 105
 */
import java.util.*;

public class ValidSubString {
    static int findMaxLen(String s) {
        // code here
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        int max = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {
                    int len = i - stack.peek();
                    max = Math.max(max, len);
                }
            }
        }
        return max;
    }

    public static void main(String args[]) {
        System.out.println(findMaxLen("(())()())"));
    }
}
