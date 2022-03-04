"""
Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

                    1       <- 
                2       3       <- 
                5           4       <-

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
                    1       <- 
                2       3       <- 
                5           4       <-
q = []
prev = 4
items = [1, 3, 4]
"""
def rightSideView(root: TreeNode) -> List[int]:
    if not root: return []

    dummy = TreeNode()
    q = [root, dummy]
    items = []
    
    while q:
        node = q.pop(0)
        if node == dummy:
            if q: q.append(dummy)
            items.append(prev.val)
            continue
        prev = node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return items

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))

print(rightSideView(root))