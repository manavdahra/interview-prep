"""
K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""

from heapq import heappop, heappush
from math import sqrt
from typing import List


def findKClosestPoints(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for point in points: # O(nlogk)
        dist = sqrt(point[0]**2 + point[1]**2)
        heappush(heap, (-dist, point)) # O(logk)
        while len(heap) > k:
            heappop(heap)
    ans = []
    for dist, point in heap:
        ans.append(point)
    
    return ans

testCases = [
    [[[1,3],[-2,2]], 1, [[-2,2]]],
    [[[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]]],
]

for t in testCases:
    actual = findKClosestPoints(t[0], t[1])
    print('Expected: {}, Actual: {}'.format(t[2], actual))
