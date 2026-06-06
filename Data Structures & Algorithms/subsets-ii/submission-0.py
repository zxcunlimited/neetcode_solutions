class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # неэфективный backtrack с превращением множества в список после решения
        self.res = set()
        def backtrack(i, cur):
            if i == len(nums):
                self.res.add(tuple(cur))
                return

            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()
            backtrack(i + 1, cur)

        nums.sort()
        backtrack(0, [])
        return [list(s) for s in self.res]