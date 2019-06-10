package booking;

import java.util.HashMap;
import java.util.Map;

/**
 * Author: B0204046
 * Date: 09/06/19 19:23
 */
public class RoutingNumbers {

    private static int[] arr = new int[3];

    public static void main(String[] args) {
        Map<Key, String> routing = new HashMap<>();

        arr[0] = 123400; // BOA
        arr[1] = 123500; // GCU
        arr[2] = 123600;

        routing.put(new Key(123400), "BOA");
        routing.put(new Key(123500), "GCU");

        System.out.println(routing);
        System.out.println(routing.get(new Key(123450)));
    }

    public static class Key {
        private Integer val;

        public Key(int k) {
            this.val = k;
        }

        /**
         * Determining the bucket
         * @return
         */
        @Override
        public int hashCode() {
            int h = closestValueInArray(this.val);
            System.out.println("hash code: " + h);
            return h;
        }

        @Override
        public boolean equals(Object obj) {
            if (!(obj instanceof Key)) {
                return false;
            }
            int h = closestValueInArray(this.val);
            if (((Key) obj).val != h) {
                return false;
            }
            return true;
        }

        private int closestValueInArray(int i) {
            // finding closest largest value in the array compared to i. algo binary search
            int index = 0;
            while (arr[index] <= i) {
                index++;
            }
            return index > 0 ? arr[index - 1]: -1;
        }

        @Override
        public String toString() {
            return "Key{" +
                    "val=" + val +
                    '}';
        }
    }
}
