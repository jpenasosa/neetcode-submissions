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
        intervals.sort(key=lambda i: (i.start, i.end))
        max_rooms = 0
        rooms = []

        for interval in intervals:
            while rooms and interval.start >= rooms[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, interval.end)
            max_rooms = max(max_rooms, len(rooms))

        return max_rooms
