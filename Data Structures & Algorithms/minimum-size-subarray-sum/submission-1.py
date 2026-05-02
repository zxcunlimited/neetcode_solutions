class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_l = float("inf")
        l = 0
        cur_sum = 0
        for r in range(0, len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                min_l = min(min_l, r - l + 1)
                cur_sum -= nums[l]
                l += 1

        if min_l == float("inf"):
            return 0
        return min_l