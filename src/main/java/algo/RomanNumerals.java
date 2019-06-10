package algo;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Author: B0204046
 * Date: 31/01/19 19:20
 */
public class RomanNumerals {

    private static final Map<Integer, String> decimalToRoman = new LinkedHashMap<>();

    static {
        decimalToRoman.put(1, "I");
        decimalToRoman.put(4, "IV");
        decimalToRoman.put(5, "V");
        decimalToRoman.put(9, "IX");
        decimalToRoman.put(10, "X");
        decimalToRoman.put(40, "XL");
        decimalToRoman.put(50, "L");
        decimalToRoman.put(90, "XC");
        decimalToRoman.put(100, "C");
        decimalToRoman.put(400, "CD");
        decimalToRoman.put(500, "D");
        decimalToRoman.put(900, "CM");
        decimalToRoman.put(1000, "M");
    }

    public static void main(String[] args) {
        System.out.println(toRomanNumeral(3549));
    }

    private static String toRomanNumeral(int N) {
        int k = findClosestkey(N);
        if (k == N) {
            return decimalToRoman.get(k);
        }

        return decimalToRoman.get(k) + toRomanNumeral(N - k);
    }

    private static int findClosestkey(int N) {
        int k = -1;
        for (Map.Entry<Integer, String> e: decimalToRoman.entrySet()) {
            if (e.getKey() > N) {
                break;
            }
            k = e.getKey();
        }
        return k;
    }
}
