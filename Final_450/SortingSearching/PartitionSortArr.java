/*
 Partitioning and Sorting Arrays with Many Repeated Entries with Java Examples
 
 */

class PartitionSortArr {
    static void swap(int arr[], int i, int j) {
        if (i != j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    /*
     * normal quickSort partition mthod
     * 
     * int partition(int arr[], int low, int high) { int pivot = arr[high]; int i =
     * low - 1; for (int j = low; j < high; j++) { if (arr[j] < pivot) { i += 1;
     * swap(arr, i, j); } } swap(arr, i + 1, high); return i + 1;
     * 
     * }
     * 
     * 
     * 
     * void quickSort(int arr[], int low, int high) { if (low < high) { int pi =
     * partition(arr, low, high); quickSort(arr, low, pi - 1); quickSort(arr, pi +
     * 1, high);
     * 
     * } }
     */

    public static int[] partition(int[] input, int begin, int end) {
        int cur = begin;
        int val = input[begin];

        while (cur <= end) {
            if (input[cur] < val)
                swap(input, begin++, cur++);
            else if (input[cur] > val)
                swap(input, cur, end--);
            else
                cur++;

        }
        return new int[] { begin, end };
    }

    public static void quicksort(int[] input, int begin, int end) {
        if (end <= begin)
            return;
        int m[] = partition(input, begin, end);
        quicksort(input, begin, m[0] - 1);
        quicksort(input, m[1] + 1, end);

    }

    public static void main(String args[]) {
        PartitionSortArr p = new PartitionSortArr();
        int arr[] = { 4, 4, 3, 2, 6, 4, 7 };
        int n = arr.length;
        System.out.print("the order is ");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        quicksort(arr, 0, n - 1);
        System.out.print("the sorted order is ");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}