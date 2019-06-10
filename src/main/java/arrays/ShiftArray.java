package arrays;

/**
 * Author: B0204046
 * Date: 14/01/19 16:55
 */
public class ShiftArray {

    public static void main(String[] args) {
        int [] arr = new int[] {1, 1, 2, 3, 5};

        printArr(solution(arr, 42));
    }

    private static void printArr(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static int[] solution(int[] arr, int k) {
        // write your code in Java SE 8
        if (arr == null || arr.length == 0) {
            return arr;
        }
        if (k <= 0) {
            return arr;
        }
        if (k >= arr.length) {
            k = k % arr.length;
        }
        reverseArray(arr, 0, arr.length - k - 1);
        reverseArray(arr, arr.length - k, arr.length - 1);
        reverseArray(arr, 0, arr.length - 1);
        return arr;
    }

    private static void reverseArray(int [] a, int start, int end) {
        int i = start, j = end;
        while (i <= j) {
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
            i++;
            j--;
        }
    }
}
