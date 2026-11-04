class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        res = []
        i = 0
        while i < len(intervals) - 1:
            # Overlapping intervals
            if intervals[i+1][0] <= intervals[i][1]:
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            else:
                res.append(intervals[i])
            
            i += 1
        
        res.append(intervals[i])
        return res