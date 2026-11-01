class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        mx_area = 0
        while left < right:
            height = min(heights[left], heights[right])
            area = height * (right - left)
            mx_area = max(area, mx_area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return mx_area