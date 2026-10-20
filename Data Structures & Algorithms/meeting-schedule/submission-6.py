"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals = sorted(intervals, key=lambda x: x.start)

        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev.start == curr.start or curr.end <= prev.end or prev.end > curr.start:
                return False

            prev = curr
        
        return True
            