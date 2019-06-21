package trees;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

public class NarryTree {

    private static Node dummy = new Node();

    /**
     *
     *                  R
     *       C1  ->     C2  ->      C3
     *
     *   c11 -> c12 -> c13 | c21 c22 c23 |  c31 c32 c33
     *
     *
     * @param args
     */
    public static void main(String[] args) {
        Node c11 = new Node();
        Node c12 = new Node();
        Node c13 = new Node();

        Node c21 = new Node();
        Node c22 = new Node();
        Node c23 = new Node();

        Node c31 = new Node();
        Node c32 = new Node();
        Node c33 = new Node();

        Node c1 = new Node();
        Node c2 = new Node();
        Node c3 = new Node();

        c1.children = Arrays.asList(c11, c12, c13);
        c2.children = Arrays.asList(c21, c22, c23);
        c3.children = Arrays.asList(c31, c32, c33);

        Node root = new Node();
        root.children = Arrays.asList(c1, c2, c3);

        bfs(root);

        System.out.println(root.children.get(0).right);
        System.out.println(root.children.get(1));

        System.out.println(root.children.get(1).right);
        System.out.println(root.children.get(2));
    }

    private static void bfs(Node root) {
        Queue<Node> queue = new ArrayDeque<>();
        queue.add(root);
        queue.add(dummy);
        while (!queue.isEmpty()) {
            Node n = queue.poll();
            if (n == dummy) {
                continue;
            }
            Node prevSibling = null;
            if (n.children != null) {
                for (Node child: n.children) {
                    if (child != null) {
                        if (prevSibling != null) {
                            prevSibling.right = child;
                        }
                        queue.add(child);
                        prevSibling = child;
                    }
                }
                queue.add(dummy);
            }
        }
    }

    private static class Node {
        List<Node> children;
        Node   right;

        public Node() {
        }
    }
}
