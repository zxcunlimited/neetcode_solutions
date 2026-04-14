import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-i for i in stones]
        heapq.heapify(new_stones)
        while len(new_stones) > 1:
            x, y = -heapq.heappop(new_stones), -heapq.heappop(new_stones)
            res = max(x, y) - min(x, y)
            if res != 0:
                heapq.heappush(new_stones, -res)
        if len(new_stones) == 0: return 0
        return -new_stones[0]