"""
Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

nums[i-1] < nums[i] > nums[i+1] 

if nums[mid] < nums[mid+1]:
    lo = mid+1
else:
    hi = mid

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""

from typing import List

"""
 0,1,2,3,4,5,6
[1,2,1,3,5,6,4]

lo = 5
hi = 5
mid = 4
 
 0,1,2,3
[1,2,3,1]
lo = 2
hi = 2
mid = 2
 
 0,1
[2,1]
lo = 0
hi = 0
mid = 0

"""
def findPeak(nums: List[int]) -> int:
    lo, hi = 0, len(nums)-1

    while lo < hi:
        mid = lo + (hi-lo)//2
        if nums[mid] < nums[mid+1]:
            lo = mid+1
        else:
            hi = mid
    
    return lo

print(findPeak([1,2,1,3,5,6,4]))
print(findPeak([1,2,3,1]))
print(findPeak([2,1]))