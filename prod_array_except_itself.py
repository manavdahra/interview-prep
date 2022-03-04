"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    output = []
    prod = 1
    for i in range(len(nums)-1, -1, -1):
        prod *= nums[i]
        output.append(prod)
    output = output[::-1]
    
    left = 1
    for i in range(len(nums)):
        right = 1
        if i+1 < len(nums):
            right = output[i+1]
        if i-1 >= 0:
            left *= nums[i-1]
        output[i] = left*right
    return output

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))