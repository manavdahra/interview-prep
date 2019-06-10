package bit;

/**
 * Author: B0204046
 * Date: 14/01/19 16:29
 */
public class BinaryGap {

    public static void main(String[] args) {
        int x = 1041;
        String binaryString = Integer.toBinaryString(x);
        System.out.println(binaryString);
        System.out.println(binaryGap(binaryString));
    }

    private static int binaryGap(String binary) {
        int maxGap = 0;
        int gapCount = 0;
        char prevChar = '-';
        for (char bin: binary.toCharArray()) {
            if (prevChar == '0' && bin == '1') {
                if (gapCount > maxGap) {
                    maxGap = gapCount;
                }
            } else if (prevChar == '1' && bin == '0') {
                gapCount = 1;
            } else if (prevChar == '0' && bin == '0') {
                gapCount++;
            }

            prevChar = bin;
        }

        return maxGap;
    }
}
