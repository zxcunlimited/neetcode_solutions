class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # самое просто решение - хэш таблица
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)