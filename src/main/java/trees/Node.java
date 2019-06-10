package trees;

import java.util.ArrayList;
import java.util.List;

/**
 * Author: B0204046
 * Date: 11/11/18 00:16
 */
public class Node {
    int data;
    Node left;
    Node right;

    static int d = -1;

    public static Node createTree(int depth) {
        Node root = new Node();
        root.left = null;
        root.right = null;
        root.data = Double.valueOf(Math.random() * 10).intValue();

        if (depth == 1) {
            return root;
        }

        root.left = createTree(depth - 1);
        root.right = createTree(depth - 1);

        return root;
    }

    public static void print(Node root, int depth) {
        Node sentinel = new Node();
        List<Node> queue = new ArrayList<>();
        queue.add(root);
        queue.add(sentinel);

        while (queue.size() > 0) {
            Node r = queue.remove(0);
            if (r == sentinel) {
                System.out.println();
                depth--;
                if (queue.size() > 0)
                    queue.add(sentinel);
            } else {
                int spaces = Double.valueOf(Math.pow(2, depth - 1) - 1).intValue();
                for (int i = 0; i < spaces; i++) {
                    System.out.print(" ");
                }
                System.out.print(r != null ? r.data : " ");
                for (int i = 0; i < depth; i++) {
                    System.out.print(" ");
                }
                if (r != null) {
                    queue.add(r.left);
                    queue.add(r.right);
                }

            }

        }
    }

    public static boolean isBalanced(Node root, int depth) {
        if (root == null) {
            if (d != -1 && Math.abs(depth - d) > 1) {
                return false;
            } else {
                d = depth;
                return true;
            }
        }

        return isBalanced(root.left, depth + 1) && isBalanced(root.right, depth + 1);
    }

    public static void main(String[] args) {
        Node root = createTree(4);
        root.left.left.left = null;
        print(root, 4);
        System.out.println(isBalanced(root, 0));
    }
}
