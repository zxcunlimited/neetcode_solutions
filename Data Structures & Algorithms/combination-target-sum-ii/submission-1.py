class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res = list()
        candidates.sort()

        def backtrack(start_i, cur_list, cur_sum):
            if cur_sum == target:
                self.res.append(cur_list[:])
                return
            elif cur_sum >= target:
                return
            for i in range(start_i, len(candidates)):
                if i > start_i and candidates[i] == candidates[i - 1]:
                    continue
                cur_list.append(candidates[i])
                backtrack(i + 1, cur_list, cur_sum + candidates[i])
                cur_list.pop()

        backtrack(0, [], 0)
        return self.res