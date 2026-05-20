class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        решение через Алгоритм Кадане - эффективное решение задачи подмассива суммы
        решение базируется на двух переменных global_sum, cur_sum и простой логике:
        что нам выгоднее взять - текущий элемент и начинать создавать с него сумму, или же
        продолжать прошлую сумму добавив текущий элемент в нее
        Сложность:
        time - O(N)
        memory - O(1)
        """
        if nums == []:
            return 0
        global_sum, cur_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > cur_sum + nums[i]:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]

            if cur_sum > global_sum:
                global_sum = cur_sum
        return global_sum