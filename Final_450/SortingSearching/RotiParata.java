
/* 
PRATA - Roti Prata
no tags 

IEEE is having its AGM next week and the president wants to serve cheese prata after the meeting. The subcommittee members are asked to go to food connection and get P(P<=1000) pratas packed for the function. The stall has L cooks(L<=50) and each cook has a rank R(1<=R<=8). A cook with a rank R can cook 1 prata in the first R minutes 1 more prata in the next 2R minutes, 1 more prata in 3R minutes and so on(he can only cook a complete prata) ( For example if a cook is ranked 2.. he will cook one prata in 2 minutes one more prata in the next 4 mins an one more in the next 6 minutes hence in total 12 minutes he cooks 3 pratas in 13 minutes also he can cook only 3 pratas as he does not have enough time for the 4th prata). The webmaster wants to know the minimum time to get the order done. Please write a program to help him out.

 

Input
The first line tells the number of test cases. Each test case consist of 2 lines. In the first line of the test case we have P the number of prata ordered. In the next line the first integer denotes the number of cooks L and L integers follow in the same line each denoting the rank of a cook.

Output
Print an integer which tells the number of minutes needed to get the order done.

 

Example
Input:

3
10
4 1 2 3 4
8
1 1
8
8 1 1 1 1 1 1 1 1
Output:
12
36
1

*/
import java.util.*;

public class RotiParata {
    static boolean solve(int arr[], int p, int nc, int mid) {
        int time = 0;
        int parata = 0;
        for (int i = 0; i < nc; i++) {
            time = arr[i];
            int j = 2;
            while (time <= mid) {
                parata += 1;
                time = time + (arr[i] * j);
                j += 1;
            }
            if (parata >= p)
                return true;
        }
        return false;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 1; i <= t; i++) {
            int p = sc.nextInt();
            int nc = sc.nextInt();
            int arr[] = new int[nc];
            for (int j = 0; j < nc; j++) {
                arr[j] = sc.nextInt();
            }
            int lb = 0;
            int ub = (int) 10e8;
            int ans = 0;
            while (lb <= ub) {
                int mid = (lb + ub) / 2;
                if (solve(arr, p, nc, mid)) {
                    ans = mid;
                    ub = mid - 1;
                } else {
                    lb = mid + 1;
                }
            }

            System.out.println("Test case " + i + " is " + ans);
        }

    }
}
