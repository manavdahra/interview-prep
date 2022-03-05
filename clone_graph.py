"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

1 - 2
|   |
4 - 3

1   2

seen = {1, 2}

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
"""

class Node:
    def __init__(self, val=0, neibs=[]) -> None:
        self.val = val
        self.neibs = neibs
    
    def print(self, n):
        self.visited = set()
        self.nodes = []
        def dfs(node):
            if not node: return

            self.visited.add(node)
            self.nodes.append(node.val)

            for neib in node.neibs:
                if neib in self.visited: continue
                dfs(neib)

        dfs(self)
        print(self.nodes)

def cloneGraph(root: Node) -> Node:
    seen = {}
    def helper(node: Node) -> Node:
        if not node: return None
        if node in seen: return seen[node]

        newNode = Node(node.val)
        seen[node] = newNode

        for neib in node.neibs:
            newNode.neibs.append(helper(neib))
        
        return newNode
    
    return helper(root)

# [[2,4],[1,3],[2,4],[1,3]]
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)

one.neibs = [two, four]
print([n.val for n in one.neibs])

two.neibs = [one, three]
print([n.val for n in two.neibs])

three.neibs = [two, four]
print([n.val for n in three.neibs])

four.neibs = [one, three]
print([n.val for n in four.neibs])

cloneGraph(one).print(4)