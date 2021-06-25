
/**
 * Inserting at the end of stack with out using any other data structure
 */
import java.util.*;

public class InserBottomUseRecur {
    static Stack<Integer> stack = new Stack<>();

    Stack<Integer> insertAtBottom(Stack<Integer> stack, int N) {
        if (stack.isEmpty()) {
            stack.push(N);
        } else {
            int x = stack.pop();
            stack = insertAtBottom(stack, N);
            stack.push(x);
        }
        return stack;
    }

    public static void main(String args[]) {
        InserBottomUseRecur m = new InserBottomUseRecur();
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);
        System.out.println(stack);
        System.out.println("after inserttion");
        System.out.println(m.insertAtBottom(stack, 1));
    }
}
