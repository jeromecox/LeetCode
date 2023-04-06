'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

nums, target = [2,7,11,15], 9
nums1, target1 = [3,2,4], 6
nums2, target2 = [3,3], 6


# SOLUTION 1
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range((i+1), len(nums)):
            if nums[i] + nums[j] == target:
                return print([i, j])


two_sum(nums, target)
two_sum(nums1, target1)
two_sum(nums2, target2)


# SOLUTION 2
def two_sum1(nums, target):
    hash_map = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return print([hash_map[diff], i])
        hash_map[num] = i


two_sum1(nums, target)
two_sum1(nums1, target1)
two_sum1(nums2, target2)
