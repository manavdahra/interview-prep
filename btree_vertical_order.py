"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

                        3
                    9       20
                        15      7
{
    0: [3,15],
    -1: [9],
    1: [20],
    2: [7]
}

Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

                        3
                    9       8
                4       0       7
                        1
Explanation: 0 and 1 overalap at same position, so put 1 after 0

{
    0: [3, 0, 1],
    -1: [9],
    -2: [4],
    1: [8],
    2: [7]
}
"""
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
"""
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

                        3
                    9       8
                4       0       7
                        1
Explanation: 0 and 1 overalap at same position, so put 1 after 0

{
    0: [3, 0, 1],
    -1: [9],
    -2: [4],
    1: [8],
    2: [7]
}
keys = [-2,-1,0,1,2]
"""
def verticalTraverse(root: TreeNode) -> List[List[int]]:
    colsMap = collections.defaultdict(list)
    
    def preorder(node, r, c, colsMap):
        if not node: return

        colsMap[c].append((r, node.val))
        preorder(node.left, r+1, c-1, colsMap)
        preorder(node.right, r+1, c+1, colsMap)

    preorder(root, 0, 0, colsMap)
    keys = sorted(colsMap.keys())
    ans = []
    for k in keys:
        items = sorted(colsMap[k], key=lambda x: x[0])
        ans.append([val[1] for val in items])

    return ans

root = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))
print(verticalTraverse(root))
