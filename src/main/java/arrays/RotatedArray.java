package arrays;

/**
 * Author: B0204046
 * Date: 08/11/18 11:28
 */
public class RotatedArray {

    public static void main(String[] args) {
        int [] arr = {3, 4, 5, 6, 7, 8, 1, 2};
        System.out.println(arr[smallest(arr, 0, arr.length - 1)]);
    }

    private static int smallest(int[] arr, int s, int e) {
        if (s == e) {
            return s;
        }

        int mid = (e + s) / 2;
        int p = (mid + s) / 2;
        int q = (e + mid) / 2;

        if (arr[p] < arr[q]) {
            return smallest(arr, q + 1, e);
        } else if (arr[p] > arr[q]) {
            return smallest(arr, p + 1, q);
        }

        return p;
    }
}
