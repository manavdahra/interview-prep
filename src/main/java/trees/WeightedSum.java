package trees;

import java.util.ArrayList;
import java.util.List;

/**
 * Author: B0204046
 * Date: 09/06/19 18:31
 */
public class WeightedSum {

    public static void main(String[] args) {
        List<Object> lt = new ArrayList<>();
        lt.add(4);

        List<Object> rt = new ArrayList<>();
        rt.add(6);

        lt.add(rt);

        List<Object> input = new ArrayList<>();
        input.add(1);
        input.add(lt);

        int depth = depth(input, 1);
        System.out.println(depth);

        int sum = weightedSum(input, depth);
        System.out.println(sum);
    }

    /**
     * List<Object> input.
     * Object -> List<Integer> or Integer
     * if it is type Integer -> root element
     * else it is a child element
     * @param input
     * @return
     */
    private static int weightedSum(List<Object> input, int depth) {
        int sum = 0;
        for (Object i: input) {
            if (i instanceof Integer) {
                sum += (Integer) i * depth;
            } else {
                sum += weightedSum((List<Object>) i, depth - 1);
            }
        }
        return sum;
    }

    private static int depth(List<Object> input, int depth) {
        int max = depth;
        for (Object i: input) {
            if (!(i instanceof Integer)) {
                max = Math.max(depth((List<Object>) i, depth + 1), max);
            }
        }
        return max;
    }
}
