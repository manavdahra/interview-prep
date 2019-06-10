package stacks;

/**
 * Author: B0204046
 * Date: 10/11/18 20:09
 */
public class TowersOfHanoi {

    static Stack[] stacks = new Stack[3];

    private static boolean solve(int stackIndex) {
        if (stacks[2].getSize() == 3 && stacks[2].top.data == 1) {
            return true;
        }

        int foundIndex = -1;
        for (int i = 0; i < 3; i++) {
            if (stackIndex == i) {
                continue;
            }

            if (stacks[i].getSize() == 0 || stacks[i].top.data > stacks[stackIndex].top.data) {
                foundIndex = i;
            }
        }

        if (foundIndex == -1) {
            return false;
        }

        Item item = stacks[stackIndex].pop();
        if (item != null) {
            stacks[foundIndex].push(item.data);
        }
        return false;
    }

    private static void printStacks() {
        for (int i = 0; i < 3; i++) {
            stacks[i].print();
        }
    }

    public static void main(String[] args) {

        for (int i = 0; i < 3; i++) {
            stacks[i] = new Stack("s" + (i+1));
        }

        stacks[0].push(3);
        stacks[0].push(2);
        stacks[0].push(1);

        printStacks();
    }
}
