"""
Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

            2
        1       3
    -1        -2     4


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
"""
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
            2
        1       3
    -1        -2     4
    """
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = -sys.maxsize

        def helper(node):
            if not node: 
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            self.maxSum = max(
                self.maxSum, 
                node.val,
                left+node.val,
                node.val+right,
                left+node.val+right,
            )

            return max(
                node.val,
                left+node.val,
                node.val+right,
            )
        
        helper(root)
        return self.maxSum

root = TreeNode(2, TreeNode(1, TreeNode(-1)), TreeNode(3, TreeNode(-2), TreeNode(4)))

solution = Solution()
print(solution.maxPathSum(root))