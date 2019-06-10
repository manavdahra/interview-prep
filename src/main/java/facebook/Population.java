package facebook;

import java.util.Arrays;

/**
 * Author: B0204046
 * Date: 10/02/19 17:24
 */
public class Population {

    public static void main(String[] args) {
        System.out.println(maxPopulation(
                new int[] {2000, 1975, 1975, 1803, 1750, 1840, 1803, 1894},
                new int[] {2010, 2005, 2003, 1809, 1869, 1935, 1921, 1921})
        );
    }

    private static int maxPopulation(int[] birthYears, int[] deathYears) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int b : birthYears) {
            if (b < min) {
                min = b;
            }
        }

        for (int d : deathYears) {
            if (d > max) {
                max = d;
            }
        }

        Arrays.sort(birthYears);
        Arrays.sort(deathYears);

        int population = 0, maxPop = Integer.MIN_VALUE;
        for (int y = min; y < max; y++) {
            if (Arrays.binarySearch(birthYears, y) >= 0) {
                population++;
            }
            if (Arrays.binarySearch(deathYears, y) >= 0) {
                population--;
            }

            System.out.println("Year: " + y + " population: " + population);
            if (maxPop < population) {
                maxPop = population;
            }
        }
        return maxPop;
    }
}
