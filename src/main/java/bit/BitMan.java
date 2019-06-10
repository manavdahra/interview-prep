package bit;

/**
 * Author: B0204046
 * Date: 08/11/18 13:20
 */
public class BitMan {

    public static void main(String[] args) {
        int val = 0;
        for (int i = 0; i < 26; i++) {
            val |= 1 << i;
        }
        System.out.println(val);
    }
}
