class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        def combs(cur, idx):
            if len(cur) == k:
                self.res.append(cur)
                return
            while idx <= n:
                combs(cur + [idx], idx + 1)
                idx += 1
        combs([], 1)
        return self.res