public class SpclStack {
    public void push(int a, Stack<Integer> s) {
        // add code here.
        if (s.isEmpty()) {
            s.push(a);
        } else {
            int min = Math.min(s.peek().min, a);
            s.push(a);
        }
    }

    public int pop(Stack<Integer> s) {
        // add code here.
        if (!s.isEmpty()) {
            return s.pop();
        }
        return 0;
    }

    public int min(Stack<Integer> s) {
        // add code here.
        int mini = 9999999;
        Iterator value = s.iterator();
        while (value.hasNext()) {
            mini = Math.min(mini, value.next());
        }
        return mini;
    }

    public boolean isFull(Stack<Integer> s, int n) {
        // add code here.
        return (s.size() == n);
    }

    public boolean isEmpty(Stack<Integer> s) {
        // add code here.
        return (s.size() == 0);
    }
}
