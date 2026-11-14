class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda x: x[0])
        
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if prev_end > start:
                ans += 1
                prev_end = min(end, prev_end)
            else:
                prev_end = end

        return ans
