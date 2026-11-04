class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find the position of insertion
        lo, hi = 0, len(intervals) - 1
        while lo <= hi:
            mid = (lo+hi)//2
            if intervals[mid][1] < newInterval[0]:
                lo = mid + 1
            else:
                hi = mid - 1

        idx = lo

        # Insert new_interval, merging as needed
        res = intervals[:idx]
        while idx < len(intervals) and newInterval[1] >= intervals[idx][0]:
            newInterval[0] = min(intervals[idx][0], newInterval[0])
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            idx += 1
        
        res.append(newInterval)
        res.extend(intervals[idx:])
    
        return res
