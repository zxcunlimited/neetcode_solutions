class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(inter1, inter2):
            if inter1[1] < inter2[0]:
                return False
            return True 
        # самый простой брутфорс
        intervals.sort()
        i = 0
        while i != len(intervals) - 1:
            if overlap(intervals[i], intervals[i + 1]):
                start = min(intervals[i][0], intervals[i + 1][0])
                end = max(intervals[i][1], intervals[i + 1][1])
                new = [start, end]
                for _ in range(2):
                    intervals.pop(i)
                intervals.insert(i, new)
            else:
                i += 1
        return intervals