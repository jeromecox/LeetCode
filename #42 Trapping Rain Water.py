'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height1 = [4,2,0,3,2,5]


def trap_water(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    trapped_water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            trapped_water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            trapped_water += right_max - height[right]
    return print(trapped_water)


trap_water(height)
trap_water(height1)
