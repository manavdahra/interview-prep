package trees;

/**
 * Author: B0204046
 * Date: 11/11/18 10:46
 */
public class BSTFromSortedArray {

    private static Node bstFromSortedArr(int[] arr, int start, int end) {
        if (start > end) {
            return null;
        }
        if (start == end) {
            Node leaf = new Node();
            leaf.data = arr[start];
            return leaf;
        }

        Node node = new Node();
        int mid = (start + end) / 2;
        node.data = arr[mid];
        node.left = bstFromSortedArr(arr, start, mid - 1);
        node.right = bstFromSortedArr(arr, mid + 1, end);
        return node;
    }

    public static void main(String[] args) {
        int [] arr = new int[10];
        for (int i = 0; i < 10; i++) {
            arr[i] = i + 1;
        }

        for (int i = 0; i < 10; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        Node root = bstFromSortedArr(arr, 0, 9);
        Node.print(root, 4);
        System.out.println(Node.isBalanced(root, 0));
    }

}
