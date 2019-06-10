package trees;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

/**
 * Author: B0204046
 * Date: 11/11/18 11:05
 */
public class ListFromTree {

    static Node sentinel = new Node();

    private static List<List<Node>> listFromTree(Node root) {
        List<List<Node>> lolNode = new ArrayList<>();
        Queue<Node> q = new ArrayDeque<>();
        q.add(root);
        q.add(sentinel);
        int i = 0;
        while (!q.isEmpty()) {
            Node node = q.remove();
            if (node == sentinel) {
                if (!q.isEmpty()) {
                    q.add(sentinel);
                }
                i++;
            } else {
                List<Node> l = null;
                if (i >= lolNode.size()) {
                    l = new ArrayList<>();
                    lolNode.add(l);
                }

                l = lolNode.get(i);
                l.add(node);
                if (node.left != null)
                    q.add(node.left);
                if (node.right != null)
                    q.add(node.right);
            }
        }
        return lolNode;
    }

    public static void main(String[] args) {
        Node root = Node.createTree(5);
        Node.print(root, 5);
        List<List<Node>> lolNodes = listFromTree(root);
        for (List<Node> nodes : lolNodes) {
            for (Node node : nodes) {
                System.out.print(node.data + " ");
            }
            System.out.println();
        }
    }
}
