package arrays;

import java.util.Stack;

/**
 * Author: B0204046
 * Date: 19/01/19 15:00
 */
public class Leader {

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 2, 3, 4, 5}));
    }

    public static int solution(int[] A) {
        // write your code in Java SE 8
        int start = 0;
        int end = A.length - 1;

        int leader = leader(A, start, end);
        if (leader == -1) {
            return 0;
        }

        int leftCount = 0;
        int rightCount = 0;

        for (int i: A) {
            if (i == leader) {
                rightCount++;
            }
        }

        int count = 0;

        while (start < end) {
            if (A[start] == leader) {
                leftCount++;
                rightCount--;
            }

            if (leftCount > ((start + 1)/ 2) && rightCount > ((end - start) / 2)) {
                System.out.println(start + " " + leftCount + " " + rightCount);
                count++;
            }
            start++;
        }

        return count;
    }

    private static int leader(int[] A, int start, int end) {
        Stack<Integer> stack = new Stack<>();
        int i = start;
        while (i <= end) {
            if (stack.empty()) {
                stack.push(A[i]);
            } else {
                if (stack.peek() != A[i]) {
                    stack.pop();
                } else {
                    stack.push(A[i]);
                }
            }
            i++;
        }

        if (stack.size() == 0) {
            return -1;
        }

        int count = 0;
        i = start;
        while (i <= end) {
            if (A[i] == stack.peek()) {
                count++;
            }
            i++;
        }

        if (count > (end - start + 1) / 2) {
            return stack.peek();
        } else {
            return -1;
        }
    }
}
