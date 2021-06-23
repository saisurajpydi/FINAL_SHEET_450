
/*

SUBSUMS - Subset Sums
#binary-search #bitmasks

Given a sequence of N (1 ≤ N ≤ 34) numbers S1, ..., SN (-20,000,000 ≤ Si ≤ 20,000,000), determine how many subsets of S (including the empty one) have a sum between A and B (-500,000,000 ≤ A ≤ B ≤ 500,000,000), inclusive.

Input
The first line of standard input contains the three integers N, A, and B. The following N lines contain S1 through SN, in order.

Output
Print a single integer to standard output representing the number of subsets satisfying the above property. Note that the answer may overflow a 32-bit integer.

Example
Input:
3 -1 2
1
-2
3

Output:
5
The following 5 subsets have a sum between -1 and 2:

0 = 0 (the empty subset)
1 = 1
1 + (-2) = -1
-2 + 3 = 1
1 + (-2) + 3 = 2

*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.function.BiPredicate;

public class SubSetSumSpoj {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();

        int arr[] = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();

        System.out.println("the subset sum count is: " + getCountOfSubsets(arr, A, B));
    }

    private static long getCountOfSubsets(int[] arr, int a, int b) {
        Integer[] firstSubsetSums = getSubsetSums(arr, 0, arr.length / 2);
        Integer[] secondSubsetSums = getSubsetSums(arr, arr.length / 2 + 1, arr.length - 1);
        Arrays.sort(secondSubsetSums);

        long count = 0;
        for (int i = 0; i < firstSubsetSums.length; i++) {
            int p = findLastIdxWithFalsePredicate(secondSubsetSums, a - firstSubsetSums[i], (sum, mark) -> sum >= mark);
            int q = findLastIdxWithFalsePredicate(secondSubsetSums, b - firstSubsetSums[i], (sum, mark) -> sum > mark);
            count += (q - p);
        }

        return count;
    }

    private static int findLastIdxWithFalsePredicate(Integer[] sums, int val, BiPredicate<Integer, Integer> pred) {
        int min = 0;
        int max = sums.length - 1;
        while (min < max) {
            int mid = min + (max - min + 1) / 2;
            if (pred.test(sums[mid], val)) {
                max = mid - 1;
            } else {
                min = mid;
            }
        }
        if (pred.test(sums[min], val))
            return -1;
        return min;
    }

    private static Integer[] getSubsetSums(int[] arr, int st, int end) {
        List<Integer> sums = new ArrayList<>();
        generateSubsetSumsRecur(arr, st, end, st, 0, sums);
        return sums.toArray(new Integer[0]);
    }

    private static void generateSubsetSumsRecur(int[] arr, int st, int end, int index, int runningSum,
            List<Integer> sums) {
        if (index == end + 1) {
            sums.add(runningSum);
            return;
        }

        generateSubsetSumsRecur(arr, st, end, index + 1, runningSum + arr[index], sums);
        generateSubsetSumsRecur(arr, st, end, index + 1, runningSum, sums);
    }
}
