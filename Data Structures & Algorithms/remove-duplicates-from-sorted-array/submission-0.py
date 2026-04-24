class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        d = {}
        while True:
            try:
                if d.get(nums[p], 0) != 0:
                    nums.remove(nums[p])
                else:
                    d[nums[p]] = 1
                    p += 1
            except IndexError:
                return len(nums)