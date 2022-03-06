"""
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]
"""

from typing import List

"""
        0,1,2,3,4,5, 6
nums = [5,7,7,7,8,8,10], k = 8
lo = 3
hi = 6
mid = 3
"""
def findFirstAndLast(nums: List[int], target: int):
    def findFirst():
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo)//2 + 1
            if nums[mid-1] < nums[mid] and nums[mid] == target:
                return mid
            elif nums[mid] >= target:
                hi = mid-1
            else:
                lo = mid
        
        if lo == hi and nums[lo] == target: return lo
        return -1
    """
            0,1,2,3,4,5, 6
    nums = [5,7,7,8,8,8,10], k = 8
    lo = 4
    hi = 6
    mid = 5
    """
    def findLast():
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo)//2
            if nums[mid] < nums[mid+1] and nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                lo = mid+1
            else:
                hi = mid
        
        if lo == hi and nums[lo] == target: return lo
        return -1
    
    return [findFirst(), findLast()]

print(findFirstAndLast([5,7,7,8,8,10], 8))
print(findFirstAndLast([5,7,7,7,8,8,10], 8))
print(findFirstAndLast([5,7,7,8,8,8,10], 8))
print(findFirstAndLast([5,7,7,8,8,8,10], 5))
print(findFirstAndLast([5,7,7,8,8,8,10], 10))
print(findFirstAndLast([], 10))