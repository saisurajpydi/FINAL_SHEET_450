import java.util.*;

public class AggresiveCows {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        ArrayList<Integer> alist = new ArrayList<>();
        while (t-- != 0) {
            int n, c;
            n = sc.nextInt();
            c = sc.nextInt();
            for (int i = 0; i < n; i++) {
                alist.add(sc.nextInt());
            }
            Collections.sort(alist);
            int low = 0, high = alist.get(n - 1), mid, best = 0;
            while (low <= high) {
                mid = (low + high + 1) / 2;
                int cnt = 1, left = 0;
                for (int i = 1; i < n && cnt < c; i++) {
                    if (alist.get(i) - alist.get(left) >= mid) {
                        left = i;
                        cnt++;
                    }
                }
                if (cnt >= c) {
                    best = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            System.out.println(" best " + best);

        }

    }

}
