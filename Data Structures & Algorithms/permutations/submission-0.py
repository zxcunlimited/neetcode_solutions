class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        self.n = len(nums)
        def backtrack(cur_nums, picked):
            if len(cur_nums) == self.n:
                self.res.append(cur_nums[:])
                return
            for i in range(self.n):
                if picked[i] == False:
                    cur_nums.append(nums[i % self.n])
                    picked[i] = True
                    backtrack(cur_nums, picked)
                    cur_nums.pop()
                    picked[i] = False

        backtrack([], [False for _ in range(self.n)])
        return self.res