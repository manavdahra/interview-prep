"""
Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Input: root = [2,1,3]
Output: [2,1,3]
"""
from plot_tree import TreeNode

def balance(root: TreeNode) -> TreeNode:
    values = []
    def inorder(node):
        if not node: 
            return 
        
        inorder(node.left)
        values.append(node.val)
        inorder(node.right)
    
    def createBST(beg, end):
        if beg > end: return None
        if beg == end: return TreeNode(values[beg])

        mid = (beg + end) // 2
        node = TreeNode(values[mid])
        node.left = createBST(beg, mid-1)
        node.right = createBST(mid+1, end)
        return node
    
    inorder(root)
    return createBST(0, len(values)-1)

"""
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
"""

root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5)))))
root.visualise()
print('############ Balanced ###############')
balance(root).visualise()