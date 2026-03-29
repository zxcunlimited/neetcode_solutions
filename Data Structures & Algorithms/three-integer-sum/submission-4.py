class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        d = {i: -1 for i in nums}
        for i in range(n):
            for j in range(i + 1, n):
                temp_sum = nums[i] + nums[j]
                try:
                    if d[(0 - temp_sum)] != -1:
                        ans.append(sorted([nums[i], nums[j], (0 - temp_sum)]))
                except:
                    continue
                d[nums[j]] = j
            d = {i: -1 for i in nums}
        res = []
        for i in ans:
            if i not in res:
                res.append(i)
        return res