'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''


nums = [1,2,3,4]
nums1 = [-1,1,0,-3,3]


def product_except_self(nums):
    output = [1] * (len(nums))

    left = 1
    for i in range(len(nums)):
        output[i] = left
        left *= nums[i]
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= right
        right *= nums[i]
    return print(output)


product_except_self(nums)
product_except_self(nums1)
