class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False] * len(nums)
        can_reach[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            end_idx = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end_idx):
                if can_reach[j]:
                    can_reach[i] = True
                    break
        return can_reach[0]