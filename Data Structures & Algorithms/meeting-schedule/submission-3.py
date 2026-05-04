"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start = [meeting.start for meeting in intervals]
        end = [meeting.end for meeting in intervals]

        start.sort()
        end.sort()
        n = len(intervals)
        start_idx = 1
        end_idx = 0

        while start_idx < n:
            if start[start_idx] < end[end_idx]:
                return False
            start_idx += 1
            end_idx += 1

        return True