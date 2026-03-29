import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # рабочее решение но из-за использование массива похуже, лучше использовать постоянно меняющийся минимум
        # l, r = 1, max(piles)
        # res = []
        # while l < r:
        #     mid = (l + r) // 2
        #     count = 0
        #     for i in piles:
        #         count += math.ceil(i / mid)
        #     if count > h:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        #         res.append(mid)
        # count = 0
        # mid = (l + r) // 2
        # for i in piles:
        #     count += math.ceil(i / mid)
        # if count <= h:
        #     res.append(mid)
        # if res != []:
        #     return min(res)
        # else:
        #     return (l + r) // 2

        # а вот это уже хорошее решение
        l, r = 1, max(piles)
        res = r
        while l < r:
            mid = (l + r) // 2
            count = 0
            for i in piles:
                count += math.ceil(i / mid)
            if count > h:
                l = mid + 1
            else:
                r = mid - 1
                if mid < res:
                    res = mid
        count = 0
        mid = (l + r) // 2
        for i in piles:
            count += math.ceil(i / mid)
        if count <= h:
            if mid < res:
                res = mid
        return res