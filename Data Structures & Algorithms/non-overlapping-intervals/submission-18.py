class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])

        # Greedy: Keep interval that ends sooner as it gives more options
        ans = 0
        prev = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev:
                ans += 1
            else:
                prev = end

        return ans
