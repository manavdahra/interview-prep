"""
LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the cache class:

cache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Input
["cache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
cache cache = new cache(2);
cache.put(1, 1); // cache is {1=1}
cache.put(2, 2); // cache is {1=1, 2=2}
cache.get(1);    // return 1
cache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
cache.get(2);    // returns -1 (not found)
cache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
cache.get(1);    // return -1 (not found)
cache.get(3);    // return 3
cache.get(4);    // return 4
"""
class Node:
    def __init__(self, key=-1, val=0, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LruCache:
    def __init__(self, cap) -> None:
        self.cap = cap
        self.head = Node()
        self.tail = Node()
        self.map = {}
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def put(self, key: int, val: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = val
            self.removeNode(node)
            self.putInFront(node)
        else:
            self.map[key] = Node(key, val)
            self.putInFront(self.map[key])
        
        if len(self.map) > self.cap:
            node = self.tail.prev
            self.removeNode(node)
            del self.map[node.key]
    
    def get(self, key: int) -> int:
        if key not in self.map: return -1
        
        node = self.map[key]
        self.removeNode(node)
        self.putInFront(node)
        return node.val
    
    def removeNode(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def putInFront(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

cache = LruCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))