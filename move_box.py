"""
Minimum Moves to Move a Box to Their Target Location

A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following rules:

The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
The character '.' represents the floor which means a free cell to walk.
The character '#' represents the wall which means an obstacle (impossible to walk there).
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.


Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.

rb, cb
rs, cs
new player pos = (rb, cb)
new box pos = (rb + (rb-rs), cb + (cb-cs))

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1

Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation: push the box down, left, left, up and up.
"""

from typing import List


"""

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
"""
def moveBox(grid: List[List[str]]) -> int:
    moves = [
        [0,1],
        [1,0],
        [0,-1],
        [-1,0],
    ]

    player, box, target = None, None, None

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'T':
                target = (i, j)
                grid[i][j] = '.'
            if grid[i][j] == 'B':
                box = (i, j)
                grid[i][j] = '.'
            if grid[i][j] == 'S':
                player = (i, j)
                grid[i][j] = '.'

    if box == target: return 0

    def invalidCell(pos):
        return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(grid) or pos[1] >= len(grid[pos[0]]) or grid[pos[0]][pos[1]] != '.'

    def canAccess(dest, box, src):
        q = [src]
        visited = set()
        while q:
            pos = q.pop(0)
            if invalidCell(pos): continue
            if pos in visited: continue
            if pos == box: continue
            if pos == dest: return True
            visited.add(pos)

            for move in moves:
                x = pos[0] + move[0]
                y = pos[1] + move[1]
                q.append((x, y))
        
        return False
    
    visited = set()
    q = [(box, player, 0)]
    while q:
        box, player, pushes = q.pop(0)
        if box == target:
            return pushes
        if (box, player) in visited: continue
        visited.add((box, player))

        for move in moves:
            newBox = (box[0] + move[0], box[1] + move[1])
            dest = (box[0] - move[0], box[1] - move[1])
            if invalidCell(newBox): continue
            if (newBox, box) in visited: continue
            if not canAccess(dest, box, player): continue
            q.append((newBox, box, pushes+1))
    
    return -1


print(moveBox([["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]))

print(moveBox([["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]))

print(moveBox([["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]))
