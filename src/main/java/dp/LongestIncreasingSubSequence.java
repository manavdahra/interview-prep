package dp;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * Author: Manav
 * Date: 10/07/18 15:32
 */
public class LongestIncreasingSubSequence {

    private static Random random = new Random();

    private static List<Integer> arr = new ArrayList<>();

    static {
        arr.add(50);
        arr.add(3);
        arr.add(10);
        arr.add(7);
        arr.add(40);
        arr.add(80);
        // arr.add(3);
        // arr.add(10);
        // arr.add(2);
        // arr.add(1);
        // arr.add(20);
    }
    //{3, 10, 2, 1, 20}

    private static int max = 1;

    public static void main(String[] args) {
        // for (int i = 0; i < 10; i++) {
        //   arr[i] = Double.valueOf(random.nextDouble() * 100).intValue();
        // }

        arr.forEach(item -> System.out.print(item + " "));
        System.out.println();

        List<Integer> a = lis(arr, arr.size());

        a.forEach(item -> System.out.print(item + " "));
        System.out.println();

        System.out.println(max);
    }

    private static List<Integer> lis(List<Integer> arr, int length) {
        if (length == 1) {
            List<Integer> l = new ArrayList<>();
            l.add(arr.get(0));
            return l;
        }

        List<Integer> _lis = new ArrayList<>();
        for (int i = 1; i < length; i++) {
            List<Integer> lis = lis(arr, i);
            if (lis.size() + 1 > _lis.size() && arr.get(length - 1) > (lis.size() > 0 ? lis.get(lis.size() - 1) : 0)) {
                _lis = lis;
                _lis.add(arr.get(length - 1));

            }
        }

        if (max < _lis.size()) {
            max = _lis.size();
        }

        return _lis;
    }

}
