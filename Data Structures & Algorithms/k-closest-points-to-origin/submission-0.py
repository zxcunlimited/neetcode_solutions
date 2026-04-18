from heapq import *
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x, y):
            return math.sqrt(x ** 2 + y ** 2) 

        heap = []
        for el in points:
            heappush(heap, (distance(el[0], el[1]), el))

        return [heappop(heap)[1] for _ in range(k)]