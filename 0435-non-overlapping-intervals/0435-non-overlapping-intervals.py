class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0

        intervals.sort(key=lambda x: x[1])

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                result += 1
            else:
                prev_end = intervals[i][1]
        return result