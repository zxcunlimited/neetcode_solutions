class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # рабочий метод но не для всех случаем
        # контр-пример: [2, 3, 5], 6: алгоритм сразу берет 5 хотя надо два раза по 3
        # res = 0
        # coins.sort(reverse = True)
        # i = 0
        # while amount > 0:
        #     if amount < 0 or i >= len(coins):
        #         return -1
        #     if amount >= coins[i]:
        #         amount -= coins[i]
        #         res += 1
        #     elif amount < coins[i]:
        #         i += 1
        # return res
        '''
        один из вариантов решения проблемы - запуск для каждого количества монет
        тоже почти что работает, но контрпримером является случай, когда нужно рассчитать наперед
        сколько можно взять денег того или иного количества чтобы можно было взять монеты и дойти
        до ответа
        к примеру, [4, 7, 10], 31
        10 + 10 + 10 ответ не дадут
        10 + 10 + 7 + 4 - минимальный случай
        '''
        # def count(cur_amount, i, cur_money):
        #     while cur_amount > 0:
        #         if cur_amount < 0 or i >= len(coins):
        #             return
        #         if cur_amount >= coins[i]:
        #             cur_amount -= coins[i]
        #             cur_money += 1
        #         elif cur_amount < coins[i]:
        #             i += 1
        #     self.res = min(self.res, cur_money)
        # self.res = float("+inf")
        # coins.sort(reverse = True)
        # for j in range(len(coins)):
        #     count(amount, j, 0)
        # return self.res if self.res != float("+inf") else -1

        # и как всегда рабочий вариант - кэширование 
        cache = [float("inf") if i not in coins else 1 for i in range(amount + 1)]
        cache[0] = 0
        coins.sort()
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    cache[i] = min(cache[i], cache[i - coin] + 1)
        return cache[-1] if cache[-1] != float("inf") else -1
