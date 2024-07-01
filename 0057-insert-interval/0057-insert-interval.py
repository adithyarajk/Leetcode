class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        
        for start, end in sorted(intervals+[newInterval]):
            if result and result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])

        return result