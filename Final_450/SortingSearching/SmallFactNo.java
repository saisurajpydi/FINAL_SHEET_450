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
