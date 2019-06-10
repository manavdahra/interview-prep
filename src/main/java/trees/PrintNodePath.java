package trees;

/**
 * Author: B0204046
 * Date: 11/11/18 13:44
 */
public class PrintNodePath {

    private static void printPaths(Node root, int sum, StringBuilder sb) {
        if (root == null) {
            return;
        }

        if (root.data == sum) {
            System.out.println(sb);
            return;
        }

        StringBuilder old = new StringBuilder(sb);

        sb.append(root.data);
        sb.append(" -> ");
        StringBuilder newSb = new StringBuilder(sb);

        sb = newSb;
        printPaths(root.left, sum - root.data, sb);

        sb = old;
        printPaths(root.left, sum, sb);

        sb = newSb;
        printPaths(root.right, sum - root.data, sb);

        sb = old;
        printPaths(root.right, sum, sb);
    }

    public static void main(String[] args) {
        Node root = Node.createTree(5);
        Node.print(root, 5);
        printPaths(root, 3, new StringBuilder());
    }
}
