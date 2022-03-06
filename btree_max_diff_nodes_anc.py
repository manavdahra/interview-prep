"""
Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

there are at least 2 nodes in the B-tree
0 <= node.val <= 10^5

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    """
                        8
                    3       10
                1       6
    root = [8,3,10,1,6]
    node.val = 1
    minVal = 3
    maxVal = 8
    self.maxDiff = max(8-1, 3-1)
    """
def maxDiff(root: TreeNode) -> int:
    def dfs(node, minVal, maxVal):
        if not node: return maxVal-minVal

        currMin = min(minVal, node.val)
        currMax = max(maxVal, node.val)
        left = dfs(node.left, currMin, currMax)
        right = dfs(node.right, currMin, currMax)
        return max(left, right)
    
    return dfs(root, root.val, root.val)

root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(10))
print(maxDiff(root))