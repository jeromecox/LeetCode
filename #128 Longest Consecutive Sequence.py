'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

nums = [100,4,200,1,3,2]
nums1 = [0,3,7,2,5,8,4,6,0,1]
nums2 = []
nums3 = [1,2,0,1]


# SOLUTION #1
def longest_consecutive(nums):
    if len(nums) == 0:
        return print(0)

    sort_array = sorted(nums)
    length = 1
    max_length = 1

    for i in range(1, len(sort_array)):
        if sort_array[i] == sort_array[i-1]:
            continue
        if sort_array[i] - sort_array[i-1] == 1:
            length += 1
            if length >= max_length:
                max_length = length
        else:
            length = 1

    return print(max_length)


longest_consecutive(nums)
longest_consecutive(nums1)
longest_consecutive(nums2)
longest_consecutive(nums3)
