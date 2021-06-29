
/**
 * Kadane's Algorithm Medium Accuracy: 51.0% Submissions: 96052 Points: 4 Given
 * an array arr of N integers. Find the contiguous sub-array with maximum sum.
 * 
 * 
 * Example 1:
 * 
 * Input: N = 5 arr[] = {1,2,3,-2,5} Output: 9 Explanation: Max subarray sum is
 * 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray. Example 2:
 * 
 * Input: N = 4 arr[] = {-1,-2,-3,-4} Output: -1 Explanation: Max subarray sum
 * is -1 of element (-1)
 * 
 * Your Task: You don't need to read input or print anything. The task is to
 * complete the function maxSubarraySum() which takes arr and N as input
 * parameters and returns the sum of subarray with maximum sum.
 * 
 * 
 * Expected Time Complexity: O(N) Expected Auxiliary Space: O(1)
 * 
 * 
 * Constraints: 1 ≤ N ≤ 106 -107 ≤ A[i] ≤ 107
 * 
 * 
 */

public class KadanesAlgo {

    int maxSubarraySum(int arr[], int n) {

        // Your code here
        int sum = 0;
        int max = arr[0];
        for (int i : arr) {
            sum += i;
            if (sum < i) {
                sum = i;
            }
            if (max < sum) {
                max = sum;
            }
            // or max = Math.max(max,sum)
        }
        return max;
    }

    public static void main(String args[]) {
        int arr[] = { 1, 2, 3, -2, 5 };
        int n = arr.length;
        KadanesAlgo k = new KadanesAlgo();
        System.out.println("the max sum subArray val :" + k.maxSubarraySum(arr, n));
    }

}
/**
 * SOLUTION DESCRIPTION: in variable sum we store by iterating the array and
 * checking whether the sum till i is max(for contiguous sub array sum val) or
 * the i th val is assigned to var sum, max is initially assigned with the first
 * value of array , and in each iteration checks, max not less tham sum val. and
 * the max of max and sum is prst in max. return max after complete iteration.
 */