class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = []
        self.n = len(nums)
        def back(idx, xor):
            while idx < self.n:
                temp_res = xor ^ nums[idx]
                self.res.append(temp_res)
                idx += 1
                back(idx, temp_res)

        back(0, 0)
        return sum(self.res)