"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)

        max_rooms = 0
        
        rooms = []
        intervals.sort(key=lambda x: x.start)

        for i in range(len(intervals)):
            cur = intervals[i]

            # Remove rooms that cannot possibly conflict
            while rooms and rooms[0] <= cur.start:
                heapq.heappop(rooms)

            heapq.heappush(rooms, cur.end)
            max_rooms = max(max_rooms, len(rooms))

        return max(len(rooms), max_rooms)
