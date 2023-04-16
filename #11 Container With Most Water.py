'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
height = [1,8,6,2,5,4,8,3,7]
height1 = [1,1]


# SOLUTION #1
def max_area(height):
    left, right = 0, len(height) - 1
    area = 0

    while left < right:
        area = max(area, min(height[left], height[right]) * (right - left))

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return print(area)


max_area(height)
max_area(height1)


# SOLUTION #2
def max_area1(height):
    left, right = 0, len(height) - 1
    max_height = max(height)
    area = 0

    while left < right:
        area = max(area, min(height[left], height[right]) * (right - left))

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

        if max_height * (right - left) <= area:
            break

    return print(area)


max_area1(height)
max_area1(height1)
