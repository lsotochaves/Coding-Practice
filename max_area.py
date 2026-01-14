# You are given an integer array `height` of length n. There are n vertical lines drawn such that
# the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that, together with the x-axis, form a container such that the container
# contains the maximum amount of water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            min_height = min(height[right], height[left])
            width = right - left
            current_area = min_height * width

            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
