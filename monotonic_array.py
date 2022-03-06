"""
Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

1,2,2,3,4,5
"""

from typing import List


def isMonotonic(nums: List[int]) -> bool:
    if len(nums) == 0: return True
    isInc, isDec = False, False
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            isInc = True
        if nums[i] > nums[i+1]:
            isDec = True
    return not (isInc and isDec)

print(isMonotonic([1,2,2,3,4,5]))
print(isMonotonic([1]))
print(isMonotonic([]))
print(isMonotonic([1,2,1]))
print(isMonotonic([2,1,2]))
print(isMonotonic([3,1,-1]))