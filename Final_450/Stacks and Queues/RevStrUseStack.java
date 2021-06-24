
/**
 * Reverse a string using Stack 
Easy Accuracy: 54.33% Submissions: 34151 Points: 2
You are given a string S, the task is to reverse the string using stack.

 

Example 1:


Input: S="GeeksforGeeks"
Output: skeeGrofskeeG
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function reverse() which takes the string S as an input parameter and returns the reversed string.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

 

Constraints:
1 ≤ length of the string ≤ 100
 */
import java.util.*;

class RevStrUseStack {
    Stack<Character> stack = new Stack<>();

    public String reverse(String S) {
        // code here
        for (int i = 0; i < S.length(); i++) {
            stack.push(S.charAt(i));
        }
        String result = "";
        while (!stack.isEmpty()) {
            result += stack.pop();
        }
        return result;
    }
}