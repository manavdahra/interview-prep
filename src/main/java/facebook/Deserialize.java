// package facebook;
//
// import java.util.ArrayList;
// import java.util.List;
//
// /**
//  * Author: B0204046
//  * Date: 23/04/19 22:37
//  */
// public class Deserialize {
//
//     static class Node {
//         public int val;
//         public List<Node> children;
//
//         public Node() {}
//
//         public Node(int _val, List<Node> _children) {
//             val = _val;
//             children = _children;
//         }
//     };
//
//     private static int index = 0;
//
//     public static void main(String[] args) {
//         Node root = _deserialize("[1[2][3][4]]");
//         print(root);
//     }
//
//     private static void print(Node root) {
//         if (root == null) {
//             return;
//         }
//
//         System.out.print(root.val + " ");
//         for (Node child: root.children) {
//             print(child);
//         }
//
//         System.out.println();
//     }
//
//     private static Node _deserialize(String data) {
//         Node root = null;
//         if (data.charAt(index) == '[') {
//             root = new Node();
//             String number = "";
//             while (data.charAt(index) != '[' || data.charAt(index) != ']') {
//                 number += data.charAt(index++);
//             }
//             root.val = Integer.valueOf(number);
//
//         }
//
//         if (data.charAt(index) == ']') {
//             return root;
//         }
//
//
//     }
// }
