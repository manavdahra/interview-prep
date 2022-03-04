"""
Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3]

                    1
                2       3
            4       5

Input: root = [1,2]
Output: 1

                1
            2
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def diamBTree(self):
        self.diam = 0
        def helper(node: TreeNode):
            if not node: return 0

            left = helper(node.left)
            right = helper(node.right)

            self.diam = max(self.diam, left + 1 + right)

            return 1 + max(left, right)
        helper(self)
        return self.diam-1

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(root.diamBTree())