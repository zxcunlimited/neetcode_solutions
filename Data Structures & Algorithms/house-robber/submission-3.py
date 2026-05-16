class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        cache = nums[:2] + ([-1] * (len(nums) - 2))
        for i in range(2, len(nums)):
            cache[i] = nums[i] + max(cache[:i - 1])
        return max(cache[-1], cache[-2])