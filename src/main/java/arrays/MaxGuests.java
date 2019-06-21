package arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class MaxGuests {

    /**
     * D 1 - 1
     * D 2 - 2
     * D 3 - 2
     * D 4 - 1
     * D 5 - 2
     * D 6 - 2
     * D 7 - 2
     * D 8 - 2
     * D 9 - 1
     * D 10 - 2
     * @param args
     */

    public static void main(String[] args) {
        List<Integer> checkIns = new ArrayList<>();
        List<Integer> checkOuts = new ArrayList<>();
        checkIns.addAll(Arrays.asList(1,2,10,5,5));
        checkOuts.addAll(Arrays.asList(4,5,12,9,12));
        System.out.println(maxGuestDay(checkIns, checkOuts));
    }

    private static int maxGuestDay(List<Integer> checkIns, List<Integer> checkOuts) {
        checkIns.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1.compareTo(o2);
            }
        });

        checkOuts.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1.compareTo(o2);
            }
        });

        int i = 0, j = 0;
        int count = 0, max = Integer.MIN_VALUE;
        int day = -1;
        while (i < checkIns.size() && j < checkOuts.size()) {
//            System.out.println(checkIns.get(i) + " " + checkOuts.get(j) + " " + day + " " + count);
            if (checkIns.get(i) < checkOuts.get(j)) {
                count++;
                if (max < count) {
                    max = count;
                    day = checkIns.get(i);
                }
                i++;
            } else if (checkIns.get(i) > checkOuts.get(j)) {
                count--;
                j++;
            } else {
                i++;
                j++;
            }
//            System.out.println(i + " " + j);
        }

//        System.out.println("Max guests " + max + " at day " + day);
        return day;
    }
}
