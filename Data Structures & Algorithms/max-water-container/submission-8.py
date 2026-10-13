class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            stored = width * height
            max_water = max(stored, max_water)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_water
        