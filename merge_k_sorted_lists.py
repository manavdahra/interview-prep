"""
Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""

from heapq import heappush, heappop
from typing import List


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        s = str(self.val)
        node = self.next
        while node:
            s += '->' + str(node.val)
            node = node.next
        s += '->NULL'
        print(s)

def mergeKSortedLists(lists: List[Node]) -> Node:
    
    heap = []
    index = 0
    for head in lists:
        if not head: continue
        heappush(heap, (head.val, index, head))
        index += 1
    
    dummy = Node()
    prev = dummy
    while heap:
        val, index, node = heappop(heap)
        prev.next = Node(val)
        prev = prev.next
        if node.next:
            heappush(heap, (node.next.val, index, node.next))
    
    return dummy.next

lists = [
    Node(1, Node(4, Node(5))),
    Node(1, Node(3, Node(4))),
    Node(2, Node(6)),
]
mergeKSortedLists(lists).print()
