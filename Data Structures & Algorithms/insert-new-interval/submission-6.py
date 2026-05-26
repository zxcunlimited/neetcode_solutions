class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval]
        def overlap(inter1, inter2):
            if inter2[0] > inter1[1]:
                return False
            return True

        l, r = 0, len(intervals)
        while l < r:
            mid = (l + r) // 2
            mid_inter = intervals[mid]
            if mid_inter[1] < newInterval[0]:
                l = mid + 1
            else:
                r = mid - 1
        pos = (l + r) // 2
        if not(intervals[0][1] < newInterval[0]):
            intervals.insert(0, newInterval)
        else:
            intervals.insert(pos + 1, newInterval)

        # часть из merge intervals
        # самый простой брутфорс
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