class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.res = []
        nums = sorted(nums)
        """
        введем флаги
        1 - сумма больше target
        0 - добавили
        """

        def backtrack(cur_nums, cur_sum):
            if cur_sum == target and sorted(cur_nums) not in self.res:
                self.res.append(sorted(cur_nums))
                return 0
            elif cur_sum > target:
                return 1
            i = 0
            while i < len(nums):
                res = backtrack(cur_nums + [nums[i]], cur_sum + nums[i])
                if res == 0:
                    i += 1
                elif res == 1 and (nums[i:][0]) > target - cur_sum:
                    return 1
                else:
                    i += 1

        backtrack([], 0)
        return self.res
        

