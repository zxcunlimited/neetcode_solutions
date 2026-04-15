class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # в принципе рабочее, но очень медленное решение из-за ряда причин:
        """
        - всегда начало перебора c i = 0
        - sorted при каждом решении
        """
        # self.res = []
        # nums = sorted(nums)
        # """
        # введем флаги
        # 1 - сумма больше target
        # 0 - добавили
        # """

        # def backtrack(cur_nums, cur_sum):
        #     if cur_sum == target and sorted(cur_nums) not in self.res:
        #         self.res.append(sorted(cur_nums))
        #         return 0
        #     elif cur_sum >= target:
        #         return 1
        #     i = 0
        #     while i < len(nums):
        #         res = backtrack(cur_nums + [nums[i]], cur_sum + nums[i])
        #         if res == 0:
        #             i += 1
        #         elif res == 1 and (nums[i:][0]) > target - cur_sum:
        #             return 1
        #         else:
        #             i += 1

        # backtrack([], 0)
        # return self.res
        
        self.res = []
        nums.sort()

        def backtrack(start_i, cur_list, cur_sum):
            if cur_sum == target:
                self.res.append(cur_list[:])
                return
            elif cur_sum >= target:
                return
            for i in range(start_i, len(nums)):
                cur_list.append(nums[i])
                backtrack(i, cur_list, cur_sum + nums[i])
                cur_list.pop()

        backtrack(0, [], 0)
        return self.res
