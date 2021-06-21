public class FindPivotInSortArr {
    static int binarySearch(int arr[], int n) {
        if (n == 0)
            return -1;
        if (arr[0] <= arr[n - 1])
            return 0;
        int start = 0, end = n - 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] > arr[mid + 1])
                return mid + 1;
            else if (arr[start] <= arr[mid]) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }

        }
        return 0;
    }

    public static void main(String args[]) {
        int arr[] = { 73, 85, 94, 21, 27, 34, 47, 54, 66 };
        int n = arr.length;
        System.out.println("index of pivot is " + binarySearch(arr, n));
    }
}
