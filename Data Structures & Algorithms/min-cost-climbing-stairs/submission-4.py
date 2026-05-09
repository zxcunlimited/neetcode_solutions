class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # backtracking, рабочий но ожидаемо долгий
        # self.res = float("inf")
        # def dfs(stairs, cur):
        #     if len(stairs) <= 1:
        #         self.res = min(cur, self.res)
        #         return
        #     dfs(stairs[1:], cur + stairs[0])
        #     dfs(stairs[2:], cur + stairs[1])
        # dfs(cost, 0)
        # return self.res

        # а вот вариант получше
        if len(cost)==3:
            return min(cost[1], cost[0] + cost[2])
        elif len(cost) <= 2:
            return min(cost)
        cache = cost[:2] + [0 for _ in range(len(cost) - 2)]
        for i in range(2, len(cost)):
            cache[i] = cost[i] + min(cache[i - 1], cache[i - 2])
        # for x in cache:
        #     print(str(x).ljust(3), end=" ")
        # print()
        # for x in cost:
        #     print(str(x).ljust(3), end=" ")
        # print()
        return min(cache[-1], cache[-2])