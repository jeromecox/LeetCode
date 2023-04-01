def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    i = 0
    j = len(nums) - 1
    while i <= j:
        k = int((i + j) / 2)
        if nums[k] == target:
            return print(k)
        elif nums[k] < target:
            i += 1
        else:
            j -= 1
    return print(-1)


nums = [-1,0,3,5,9,12]
target = 9
target1 = 8
target2 = 13
target3 = 3
target4 = -5


search(nums, target)
search(nums, target1)
search(nums, target2)
search(nums, target3)
search(nums, target4)
