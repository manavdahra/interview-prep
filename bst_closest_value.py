"""
Closest Binary Search Tree Value

Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Input: root = [1], target = 4.428571
Output: 1
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def findClosestValue(root: TreeNode, target: float) -> int:
    def traverse(node):
        if not node: return 10**9

        closestValue = node.val
        minDiff = abs(node.val - target)
        
        if node.val > target:
            left = traverse(node.left)
            if minDiff > abs(left-target):
                closestValue = left
        elif node.val < target:
            right = traverse(node.right)
            if minDiff > abs(right-target):
                closestValue = right
        
        return closestValue
    return traverse(root)

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))

print(findClosestValue(root, 3.714286))
print(findClosestValue(TreeNode(1), 4.428571))