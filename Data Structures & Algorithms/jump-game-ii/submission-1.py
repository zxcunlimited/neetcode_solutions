class Solution:
    def jump(self, nums: List[int]) -> int:
        dist = [float("inf")] * len(nums)
        dist[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                dist[j] = min(dist[j], 1 + dist[i])
        return dist[-1]