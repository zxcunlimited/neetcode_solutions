class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums.pop(0)
        while nums:
            res = res ^ nums.pop(0)
        return res