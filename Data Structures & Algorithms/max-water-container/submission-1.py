class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        max_amount = 0
        while l < r:
            max_amount = max((r - l) * min(heights[l], heights[r]), max_amount)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_amount