from heapq import *

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) < 2:
            return True
        
        ints = []
        for interval in intervals:
            heappush(ints, (interval.start, interval.end))

        start, end = heappop(ints)
        while ints:
            cur_start, cur_end = heappop(ints)
            if cur_start >= end:
                start = cur_start
                end = cur_end
            else:
                return False
        return True