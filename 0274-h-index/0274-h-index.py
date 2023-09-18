class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 0, 1, 3, 5, 6
        citations.sort()
        h = 0
        found = False
        n = len(citations)
        for index in range(n):
            if citations[index] + index <= n:
                h = max(h, citations[index])
                found = True
            else:
                h = max(h, n - index)
                found = True
        return h