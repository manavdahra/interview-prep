"""
Robot Room Cleaner

You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.

Custom testing:

The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position.

Input: room = [
    [1,1,1,1,1,0,1,1],
    [1,1,1,1,1,0,1,1],
    [1,0,1,1,1,1,1,1],
    [0,0,0,1,0,0,0,0],
    [1,1,1,1,1,1,1,1]
], row = 1, col = 3
Output: Robot cleaned all rooms.
Explanation: All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.

Input: room = [[1]], row = 0, col = 0
Output: Robot cleaned all rooms.

"""

from typing import List

class Robot:
    def __init__(self, row: int, col: int, grid: List[List[int]]) -> None:
        self.grid = grid
        self.row = row
        self.col = col
        self.directions = [
            [-1,0], # u
            [0,1], # r
            [1,0], # d
            [0,-1], # l
        ]
        self.dir = 0

    def move(self) -> bool:
        toMove = self.directions[self.dir]
        row = self.row + toMove[0]
        col = self.col + toMove[1]
        if row < 0 or col < 0 or row >= len(self.grid) or col >= len(self.grid[0]) or self.grid[row][col] == 0:
            return False
        self.row = row
        self.col = col
        return True
    
    def turnLeft(self):
        self.dir = (self.dir - 1)%len(self.directions)

    def turnRight(self):
        self.dir = (self.dir + 1)%len(self.directions)

    def clean(self):
        self.grid[self.row][self.col] = -1

def cleanRooms(robot: Robot):

    directions = [
        [-1,0], # u
        [0,1], # r
        [1,0], # d
        [0,-1], # l
    ]

    def goback():
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    visited = set()
    def dfs(r, c, d):
        visited.add((r, c))
        robot.clean()

        for i in range(4):
            move = directions[(d + i) % 4]
            x = r + move[0]
            y = c + move[1]
            
            if not (x, y) in visited and robot.move():
                dfs(x, y, (d + i) % 4)
                goback()
            
            robot.turnRight()
        
    
    dfs(0, 0, 0)

robot = Robot(1, 3, [
    [1,1,1,1,1,0,1,1],
    [1,1,1,1,1,0,1,1],
    [1,0,1,1,1,1,1,1],
    [0,0,0,1,0,0,0,0],
    [1,1,1,1,1,1,1,1]
])

cleanRooms(robot)
allRoomsCleaned = True
for i in range(len(robot.grid)):
    for j in range(len(robot.grid[i])):
        if robot.grid[i][j] == 1:
            allRoomsCleaned = False

if allRoomsCleaned:
    print('Robot cleaned all rooms')
else:
    print('Robot didn\'t clean all rooms')
