class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {i:-1 for i in nums}
        for i in range(len(nums)):
            temp = target - nums[i]
            try:
                if d[temp] != -1:
                    return [d[temp], i]
            except:
                continue
            d[nums[i]] = i