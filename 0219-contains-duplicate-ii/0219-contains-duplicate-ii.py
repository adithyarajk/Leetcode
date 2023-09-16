class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = dict()
        for index, ele in enumerate(nums):
            if hash_map.get(ele) is not None and abs(hash_map.get(ele) - index) <= k:
                    return True
            hash_map[ele] = index
        return False