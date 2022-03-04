"""
Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

[4,2,1,5,3]
[4,2,3,5,1]

[3,2,1]
[1,2,3]

[1,2,3]
[2,1]
"""

from typing import List


def nextPermutation(nums: List[int]):
    if len(nums) <= 1: return
    i = len(nums)-2
    while nums[i] >= nums[i+1] and i >= 0:
        i -= 1
    if i >= 0:
        j = len(nums)-1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = nums[i+1:][::-1]

input = [4,2,1,5,3]
nextPermutation(input)
print(input)

input = [3,2,1]
nextPermutation(input)
print(input)

input = [2,1]
nextPermutation(input)
print(input)

input = [1,2]
nextPermutation(input)
print(input)

input = [1]
nextPermutation(input)
print(input)

input = []
nextPermutation(input)
print(input)

input = [1,2,3,4,5,6,7,9,8]
nextPermutation(input)
print(input)