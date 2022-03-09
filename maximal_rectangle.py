"""
Maximal rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

[     0   1   2   3   4
    ["1","0","1","0","0"],   1,0,1,0,0
    ["1","0","1","1","1"],   2,0,2,1,1
    ["1","1","1","1","1"],   3,1,3,2,2
    ["1","0","0","1","0"],
]


"""

from typing import List

def maximalRectangle(matrix: List[List[int]]) -> int:

    def maxHistArea(heights: List[int]) -> int:
        maxArea = 0
        stack = [-1]

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxArea = max(maxArea, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        
        while stack[-1] != -1:
            maxArea = max(maxArea, heights[stack.pop()]*(len(heights)-stack[-1]-1))
        
        return maxArea
        
    dp = [0]*len(matrix[0])
    maxArea = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

        maxArea = max(maxArea, maxHistArea(dp))
    
    return maxArea

print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))