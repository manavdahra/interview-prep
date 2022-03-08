"""
Split Array with Equal Sum

Given an integer array nums of length n, return true if there is a triplet (i, j, k) which satisfies the following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
The sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) is equal.
A subarray (l, r) represents a slice of the original array starting from the element indexed l to the element indexed r.

Input: nums = [1,2,1,2,1,2,1]
Output: true
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1

Input: nums = [1,2,1,2,1,2,1,2]
Output: false
"""

from typing import List

def splitArrayEqual(nums: List[int]):
    if len(nums) < 7: return False

    prefix = []
    tot = 0
    for num in nums:
        tot += num
        prefix.append(tot)
    
    for j in range(3, len(nums)-3):
        sumSet = set()
        for i in range(1, j-1):
            if prefix[j-1] - prefix[i] == prefix[i-1]:
                sumSet.add(prefix[i-1])
        
        for k in range(j+2, len(nums)-1):
            if prefix[k-1] - prefix[j] == tot - prefix[k] and tot - prefix[k] in sumSet:
                return True
    
    return False

print(splitArrayEqual([1,2,1,2,1,2,1]))
print(splitArrayEqual([1,2,1,2,1,2,1,2]))
print(splitArrayEqual([1,-2,-6,-6,-5,6,4,-10,-9,-5,-1,3,8,-7,7,3,10,9,-6,7,0,9,0]))