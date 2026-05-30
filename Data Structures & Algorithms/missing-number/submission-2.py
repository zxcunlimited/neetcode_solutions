class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        num = 0
        for i in range(len(nums)):
            if num != nums[i]:
                break
            num += 1
        return num