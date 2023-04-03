'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

test_nums = [1, 2, 3, 1]
test_nums1 = [1, 2, 3, 4]
test_nums2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


# SOLUTION #1
def contains_duplicate(nums):
    test_set = set()

    for num in nums:
        if num in test_set:
            return print(True)
        test_set.add(num)

    return print(False)


contains_duplicate(test_nums)
contains_duplicate(test_nums1)
contains_duplicate(test_nums2)


# SOLUTION #2
def contains_duplicate1(nums):
    nums.sort()
    i = 0

    while i < (len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return print(True)
        i += 1

    return print(False)


contains_duplicate1(test_nums)
contains_duplicate1(test_nums1)
contains_duplicate1(test_nums2)
