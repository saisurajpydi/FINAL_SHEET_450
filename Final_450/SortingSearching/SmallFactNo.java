/*
Smallest factorial number 
Easy Accuracy: 50.47% Submissions: 6317 Points: 2
Given a number n. The task is to find the smallest number whose factorial contains at least n trailing zeroes.

Example 1:

Input:
n = 1
Output: 5
Explanation : 5! = 120 which has at
least 1 trailing 0.
Example 2:

Input:
n = 6
Output: 25
Explanation : 25! has at least
6 trailing 0.

User Task:
Complete the function findNum() which takes an integer N as input parameters, and returns the answer.

Expected Time Complexity: O(log2 N * log5 N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n <= 104


*/
public class SmallFactNo {
    static boolean check(int p, int n) {
        int temp = p, count = 0, f = 5;
        while (f <= temp) {
            count += temp / f;
            f = f * 5;
        }
        return count >= n;
    }

    int findNum(int n) {
        // Complete this function
        if (n == 1)
            return 5;
        int low = 0;
        int high = 5 * n;
        while (low < high) {
            int mid = (low + high) / 2;
            if (check(mid, n)) {
                high = mid;
            } else {
                low = mid + 1;
            }

        }
        return low;
    }

    public static void main(String args[]) {
        SmallFactNo s = new SmallFactNo();
        int n = 6;
        System.out.println(s.findNum(n));
    }

}
