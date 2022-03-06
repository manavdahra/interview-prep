"""
Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Input: root = [1,2], p = 1, q = 2
Output: 1


case 1: left = None and right = None, then current node can be p or q
case 2: left = p or q and right = None, then current node can be q or p
case 3: left = None and right = p or q, then current node can be q or p
case 4: left = p and right = q or left = q and right = p, current node is lca
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def lca2(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root: return None

    left = lca2(root.left, p, q)
    right = lca2(root.right, p, q)
    if left and right:
        return root
    else:
        if root == p or root == q:
            return root
        if not left and right:
            return right
        if left and not right:
            return left
        else:
            return None

def lca1(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    parents = {}
    def traverse(node, parent):
        if not node: return

        parents[node] = parent
        traverse(node.left, node)
        traverse(node.right, node)
    traverse(root, None)

    seen = set()
    node = p
    while node:
        seen.add(node)
        node = parents[node]
    
    node = q
    while node:
        if node in seen: return node
        node = parents[node]
    
    return None

"""
[3,5,1,6,2,0,8,null,null,7,4]
p = 5, q = 1
"""
p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
q = TreeNode(1, TreeNode(0), TreeNode(8))
root = TreeNode(3, p, q)
anc = lca1(root, p, q)
print(anc.val)
anc = lca2(root, p, q)
print(anc.val)

"""
[3,5,1,6,2,0,8,null,null,7,4]
p = 5, q = 1
"""
q = TreeNode(4)
p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), q))
root = TreeNode(3, p, TreeNode(1, TreeNode(0), TreeNode(8)))
anc = lca1(root, p, q)
print(anc.val)
anc = lca2(root, p, q)
print(anc.val)