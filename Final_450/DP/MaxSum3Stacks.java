/**
 * Find maximum sum possible equal sum of three stacks Difficulty Level : Easy
 * Last Updated : 25 Mar, 2021 Given three stacks of the positive numbers, the
 * task is to find the possible equal maximum sum of the stacks with the removal
 * of top elements allowed. Stacks are represented as an array, and the first
 * index of the array represent the top element of the stack.
 * 
 * Examples:
 * 
 * Input : stack1[] = { 3, 10} stack2[] = { 4, 5 } stack3[] = { 2, 1 } Output :
 * 0 Sum can only be equal after removing all elements from all stacks.
 */
public class MaxSum3Stacks {
    static int solution(int s1[], int s2[], int s3[]) {
        int n1 = s1.length;
        int n2 = s2.length;
        int n3 = s3.length;
        int v1 = 0, v2 = 0, v3 = 0;
        for (int i = 0; i < n1; i++) {
            v1 += s1[i];
        }
        for (int i = 0; i < n2; i++) {
            v2 += s2[i];
        }
        for (int i = 0; i < n3; i++) {
            v3 += s3[i];
        }
        int t1 = 0, t2 = 0, t3 = 0;
        while (true) {
            if (t1 == n1 || t2 == n2 || t3 == n3) {
                return 0;
            }
            if (v1 == v2 && v2 == v3) {
                return v1;
            }
            if (v1 > v2 && v1 > v3) {
                v1 -= s1[t1++];
            } else if (v2 > v3 && v2 > v1) {
                v2 -= s2[t2++];
            } else if (v3 > v1 && v3 > v2) {
                v3 -= s3[t3++];
            }
        }
    }

    public static void main(String[] args) {
        int s1[] = { 3, 10 };// { 3, 2, 1, 1, 1 };
        int s2[] = { 4, 5 };// { 4, 3, 2 };
        int s3[] = { 2, 1 };// { 1, 1, 4, 1 };
        System.out.println(solution(s1, s2, s3));
    }

}
/**
 * SOLUTION DESCRIPTION: firstly find sum of each stack if sum of all stacks are
 * same return the sum val else check for the max sum stack and pop the top and
 * recursively repeat the above. time : O(N) space: constant variables. O(1)
 */