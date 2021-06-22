
/*
In-Place Merge Sort
Difficulty Level : Hard
Last Updated : 06 Jun, 2021
Implement Merge Sort i.e. standard implementation keeping the sorting algorithm as in-place. 
In-place means it does not occupy extra memory for merge operation as in the standard case.

Examples: 

Input: arr[] = {2, 3, 4, 1} 
Output: 1 2 3 4

Input: arr[] = {56, 2, 45} 
Output: 2 45 56 
*/
public class InPlaceMergeSort {
    static void merge(int arr[], int l, int m, int r) {
        int l2 = m + 1;
        if (arr[m] <= arr[l2])
            return;
        while (l <= m && l2 <= r) {
            if (arr[l] <= arr[l2]) {
                l += 1;
            } else {
                int val = arr[l2];
                int index = l2;
                while (index != l) {
                    arr[index] = arr[index - 1];
                    index -= 1;
                }
                arr[l] = val;

                l += 1;
                m += 1;
                l2 += 1;
            }
        }
    }

    static void mergesort(int arr[], int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            mergesort(arr, l, m);
            mergesort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    public static void main(String args[]) {
        int arr[] = { 2, 3, 4, 1 };
        int n = arr.length;
        System.out.println("before sort");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("\nafter sort");
        mergesort(arr, 0, n - 1);
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }

    }
}
