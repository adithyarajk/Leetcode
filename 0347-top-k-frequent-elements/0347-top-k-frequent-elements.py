from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)

        return [x[0] for x in count_map.most_common(k)]