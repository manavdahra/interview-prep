"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9

lmax = 1
leftMax = [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]

rmax = -sys.maxsize
rightMax= [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
"""

import sys
from typing import List

"""

height =  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

leftMax = [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
rightMax= [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
"""

def trapRainWater2(height: List[int]) -> int:
    left, right = 0, len(height)-1

    trap = 0
    lMax, rMax = -1, -1
    while left < right:
        if height[left] < height[right]:
            lMax = max(lMax, height[left])
            trap += lMax-height[left]
            left += 1
        else:
            rMax = max(rMax, height[right])
            trap += rMax-height[right]
            right -= 1

    return trap

def trapRainWater(height: List[int]) -> int:
    leftMax = []
    rightMax = []
    lMax = -sys.maxsize
    rMax = -sys.maxsize

    for h in height:
        lMax = max(lMax, h)
        leftMax.append(lMax)
    
    for h in height[::-1]:
        rMax = max(rMax, h)
        rightMax.append(rMax)
    
    rightMax = rightMax[::-1]

    trap = 0
    for i in range(len(height)):
        trap += min(leftMax[i], rightMax[i]) - height[i]
    return trap

print(trapRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trapRainWater2([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trapRainWater([4,2,0,3,2,5]))
print(trapRainWater2([4,2,0,3,2,5]))