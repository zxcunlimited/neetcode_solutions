class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # самое просто решение - хэш таблица
        # s = set()
        # for num in nums:
        #     if num in s:
        #         return num
        #     s.add(num)

        # но есть и крутое решение - использовать тот факт что все кроме одного числа в массиве одинаковы
        # так как все числа от 1 до n, то можно вместо самого числа ставить какой нибудь флаг
        # и если мы снова встретим эт число - то на его месте (индексе) уже будет флаг

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1