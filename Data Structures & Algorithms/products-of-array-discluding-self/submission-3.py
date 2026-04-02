import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) >= 2:
            return [0 for i in range(len(nums))]
        zero = False
        mult = 1
        prefix = 1
        for num in nums:
            if num == 0:
                zero = True
            else:
                prefix *= num
        res = []
        for num in nums:
            if zero == 1:
                if num == 0:
                    res.append(prefix)
                else:
                    res.append(0)
            else:
                res.append(prefix // num)
        return res