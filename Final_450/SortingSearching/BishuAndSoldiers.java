import java.util.*;

class BishuAndSoldiers {
    public static void valPrint(ArrayList<Integer> arr, int val[], int q) {
        int j = 0;
        int res = 0;
        while (true) {
            if (arr.get(j) <= q) {
                res = Math.max(res, arr.get(j));
            } else {
                break;
            }
            j++;
        }
        System.out.println(res + " " + val[arr.indexOf(res)]);

    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>(N);
        for (int i = 0; i < N; i++) {
            arr.add(sc.nextInt());
        }
        Collections.sort(arr);
        int j = 0;
        int val[] = new int[N];
        for (int i = 0; i < N; i++) {
            j = j + arr.get(i);
            val[i] = j;
        }
        for (int i = 0; i < N; i++) {
            System.out.println(val[i]);
        }

        int Q = sc.nextInt();
        int bis[] = new int[Q];
        for (int i = 0; i < Q; i++) {
            bis[i] = sc.nextInt();
        }
        for (int i = 0; i < Q; i++) {
            valPrint(arr, val, bis[i]);
        }
    }
}