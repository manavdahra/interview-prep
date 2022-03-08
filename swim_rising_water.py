"""
Swim in Rising Water

You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.


[
    [0,  1, 2, 3, 4],
    [24,23,22,21, 5],
    [12,13,14,15,16],
    [11,17,18,19,20],
    [10, 9, 8, 7, 6],
]

Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

swim(r, c, t) = min(
    swim(r, c+1, t),
    swim(r+1, c, t),
    swim(r, c-1, t),
    swim(r-1, c, t),
)

base case:
if r == n-1 and c == n-1: return t
if grid[r][c] > t: return swim(r, c, t+1)

"""

from heapq import heappop, heappush
from typing import List

"""
[
    [0,  1, 2, 3, 4],
    [24,23,22,21, 5],
    [12,13,14,15,16],
    [11,17,18,19,20],
    [10, 9, 8, 7, 6],
]
visited = {(0, 0), (0, 1), (0, 2)}
"""
def minTimeToSwim(grid: List[List[int]]) -> int:
    visited = set()
    n = len(grid)
    moves = [
        [0, 1],
        [1, 0],
        [0,-1],
        [-1,0],
    ]
    maxTime = 0
    pq = [(grid[0][0], 0, 0)]
    while pq:
        t, r, c = heappop(pq)
        visited.add((r, c))
        maxTime = max(maxTime, t)
        if r == n-1 and c == n-1:
            return maxTime
        
        for move in moves:
            x = r + move[0]
            y = c + move[1]
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]): continue
            if (x, y) in visited: continue
            heappush(pq, (grid[x][y], x, y))
    
    return -1

print(minTimeToSwim([
    [0,  1, 2, 3, 4],
    [24,23,22,21, 5],
    [12,13,14,15,16],
    [11,17,18,19,20],
    [10, 9, 8, 7, 6],
]))
            