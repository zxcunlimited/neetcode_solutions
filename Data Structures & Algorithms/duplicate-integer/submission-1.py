class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        better = set()
        for i in nums:
            if not(i in better):
                better.add(i)
            else:
                return True
        return False
        