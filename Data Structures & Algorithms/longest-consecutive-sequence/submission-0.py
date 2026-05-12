class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            cur = num
            while cur + 1 in nums_set:
                cur += 1
            max_len = max(max_len, cur - num + 1)
        return max_len