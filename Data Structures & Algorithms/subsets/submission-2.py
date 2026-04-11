class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        n = len(nums)

        def backtrack(cur_l, cur_i):
            self.res.append(cur_l)
            if cur_i == n:
                return
            start_i = cur_i
            while start_i != n:
                backtrack(cur_l + [nums[start_i]], start_i + 1)
                start_i += 1
            
        backtrack([], 0)
        return self.res
