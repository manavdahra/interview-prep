"""
Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

[1,0],[0,1]

indeg = [1,1]


         0,1,2
indeg = [0,0,0]

graph = {
    0: [],
    1: [0],
    2: [1]
}
Input: numCourses = 2, prerequisites = [[1,2],[0,1],[]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

import collections
from typing import List


def courseSchedule(numCourses: int, pre: List[int]) -> bool:
    indeg = [0]*numCourses
    graph = collections.defaultdict(list)

    for p in pre:
        [prev, curr] = p
        graph[curr].append(prev)
        indeg[prev] += 1
    
    q = []
    for node, ind in enumerate(indeg):
        if ind == 0:
            q.append(node)
    
    seen = set()
    while q:
        node = q.pop(0)
        seen.add(node)

        for neib in graph[node]:
            if neib in seen: continue
            indeg[neib] -= 1
            if indeg[neib] == 0:
                seen.add(neib)
                q.append(neib)
    
    for ind in indeg:
        if ind != 0: return False
    
    return True

print(courseSchedule(2, [[1,0]]))
print(courseSchedule(2, [[1,0],[0,1]]))
print(courseSchedule(3, [[1,0],[2,1]]))
print(courseSchedule(4, [[1,0],[2,1]]))
