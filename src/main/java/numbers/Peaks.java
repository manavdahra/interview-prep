package numbers;

import java.util.ArrayList;

/**
 * Author: B0204046
 * Date: 26/01/19 23:48
 */
public class Peaks {

    public static void main(String[] args) {
        Peaks peaks = new Peaks();
        System.out.println(peaks.solution(new int[]{1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2}));
    }

    public int solution(int[] A) {
        int N = A.length;

        // Find all the peaks
        ArrayList<Integer> peaks = new ArrayList<Integer>();
        for(int i = 1; i < N-1; i++){
            if(A[i] > A[i-1] && A[i] > A[i+1]) peaks.add(i);
        }

        for(int size = 1; size <= N; size++){
            if(N % size != 0) continue; // skip if non-divisible
            int find = 0;
            int groups = N/size;
            boolean ok = true;
            // Find whether every group has a peak
            for(int peakIdx : peaks){
                if(peakIdx/size > find){
                    ok = false;
                    break;
                }
                if(peakIdx/size == find) find++;
            }
            if(find != groups) ok = false;
            if(ok) return groups;
        }
        return 0;
    }
}
