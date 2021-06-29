
/**
 * Minimum removals from array to make max – min <= K
Difficulty Level : Easy
Last Updated : 12 Jun, 2021
Given N integers and K, find the minimum number of elements that should be removed, such that Amax-Amin<=K. After the removal of elements, Amax and Amin is considered among the remaining elements. 

Examples: 

Input : a[] = {1, 3, 4, 9, 10, 11, 12, 17, 20} 
          k = 4 
Output : 5 
Explanation: Remove 1, 3, 4 from beginning 
and 17, 20 from the end.

Input : a[] = {1, 5, 6, 2, 8}  K=2
Output : 3
Explanation: There are multiple ways to 
remove elements in this case.
One among them is to remove 5, 6, 8.
The other is to remove 1, 2, 5

 */
import java.util.*;

public class MinRemFrmArrMaMiK {
    static int dp[][] = new int[1001][1001];

    static int solve(int arr[], int i, int j, int k) {
        if (i >= j) {
            return 0;
        }
        if (arr[j] - arr[i] <= k) {
            return 0;
        }
        if (dp[i][j] != -1) {
            return dp[i][j];
        }
        return dp[i][j] = 1 + Math.min(solve(arr, i + 1, j, k), solve(arr, i, j - 1, k));

    }

    public static void main(String args[]) {
        int arr[] = { 1, 3, 4, 9, 10, 11, 12, 17, 20 };
        int n = arr.length;
        int k = 4;
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }
        Arrays.sort(arr);

        if (n == 1) {
            System.out.println("0");
        } else {
            System.out.println(solve(arr, 0, n - 1, k));
        }
    }
}
/**
 * SOLUTION DESCRIPTION: memoization method: 2d array initialise all valules
 * with -1 then, then base conditons and recursively find minimum val start + 1
 * and end -1 and add 1 for each call. time O(N2) space O(N2)
 */
/**
 * // Java program for the above approach import java.io.*; import java.util.*;
 * 
 * class GFG {
 * 
 * // To sort the array and return the answer static int removals(int arr[], int
 * n, int k) { // sort the array Arrays.sort(arr);
 * 
 * // fill all stated with -1 // when only one element int dp[] = new int[n];
 * Arrays.fill(dp, -1);
 * 
 * // as dp[0] = 0 (base case) so min // no of elements to be removed are // n-1
 * elements int ans = n - 1; dp[0] = 0;
 * 
 * // Iterate from 1 to n - 1 for (int i = 1; i < n; i++) { dp[i] = i; int j =
 * dp[i - 1]; while (j != i && arr[i] - arr[j] > k) { j++; } dp[i] =
 * Integer.min(dp[i], j); ans = Integer.min(ans, (n - (i - j + 1))); } return
 * ans; }
 * 
 * // Driver code public static void main(String[] args) { int a[] = { 1, 3, 4,
 * 9, 10, 11, 12, 17, 20 }; int n = a.length; int k = 4;
 * System.out.print(removals(a, n, k)); } }
 * 
 */