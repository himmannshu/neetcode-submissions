"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 0, 5, 15
        # 10, 20, 30
        """
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        """
        intervals.sort(key=lambda i : i.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False;
        return True
