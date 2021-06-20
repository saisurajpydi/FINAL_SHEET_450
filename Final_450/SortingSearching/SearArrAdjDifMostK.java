
/*
Searching in an array where adjacent differ by at most k

A step array is an array of integers where each element has a difference of at most k with its neighbor. Given a key x, we need to find the index value of x if multiple-element exist to return the first occurrence of the key.
Examples: 
 

Input : arr[] = {4, 5, 6, 7, 6}
           k = 1
           x = 6
Output : 2
The first index of 6 is 2.

Input : arr[] = {20, 40, 50, 70, 70, 60}  
          k = 20
          x = 60
Output : 5
The index of 60 is 5

 
 */
import java.util.*;

class SearArrAdjDifMostK {
    static int search(int arr[], int n, int k, int x) {
        int i = 0;
        while (i < n) {
            if (arr[i] == x) {
                return i;
            }
            i = i + Math.max(1, Math.abs(arr[i] - x) / k);
        }
        return -1;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int x = sc.nextInt();
        int k = sc.nextInt();
        System.out.println("the element prst / not " + search(arr, n, k, x));
    }
}